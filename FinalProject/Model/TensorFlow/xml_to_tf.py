import pandas as pd
import numpy as np
import csv

import argparse
import re
import os
import io
import glob
import shutil
import urllib.request
import tarfile
import xml.etree.ElementTree as ET

import tensorflow as tf


'''
Nguồn: https://towardsdatascience.com/detailed-tutorial-build-your-custom-real-time-object-detector-5ade1017fd2d#30ac
'''


def xml_to_csv(path):
	classes_names = []
	xml_list = []

	for xml_file in glob.glob(path + '/*.xml'):
		tree = ET.parse(xml_file)
		root = tree.getroot()
		for member in root.findall('object'):
			classes_names.append(member[0].text)
			value = (root.find('filename').text,
					int(root.find('size')[0].text),
					int(root.find('size')[1].text),
					member[0].text,
					int(member[4][0].text),
					int(member[4][1].text),
					int(member[4][2].text),
					int(member[4][3].text))
			xml_list.append(value)
	column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
	xml_df = pd.DataFrame(xml_list, columns=column_name)
	classes_names = list(set(classes_names))
	classes_names.sort()

	return xml_df, classes_names


'''
Nguồn: https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth/13814557
'''


def split_train_test(input_annotation, input_train_path, input_test_path, out_train_path, out_test_path):
	''' Xóa các file trong test và train'''
	for i in range(2):
		if i == 0:
			path = input_train_path
			folder = os.path.abspath(out_train_path)
		else:
			path = input_test_path
			folder = os.path.abspath(out_test_path)

		for filename in os.listdir(path):
			file_path = os.path.join(folder, filename)

			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)

	''' Copy file dựa trên file input folder'''
	for i in range(2):
		if i == 0:
			desPath = out_train_path
			filename = os.listdir(input_train_path)
		else:
			desPath = out_test_path
			filename = os.listdir(input_test_path)

		for name in filename:
			if name.endswith(".txt"):
				continue

			fullname = name.split('.')[0] + ".xml"

			fileSrc = os.path.join(os.path.abspath(input_annotation), fullname)
			fileDes = os.path.join(os.path.abspath(desPath), fullname)

			if os.path.isdir(fileSrc):
				shutil.copytree(fileSrc, fileDes, False, None)
			else:
				shutil.copy(fileSrc, fileDes)


def parser() -> None:
	parser = argparse.ArgumentParser(
		description="Converts .xlm annotations into .txt files that conform to yolo format.")
	parser.add_argument("--inputAnno", type=str, default="",
						help="The path of the input annotation folder that contains the .jpg images with their corresponding txt annotations.")
	parser.add_argument("--inputTrain", type=str, default="",
						help="The path of the output train folder in which .txt annotations will be saved.")
	parser.add_argument("--inputTest", type=str, default="",
						help="The path of the output test folder in which .txt annotations will be saved.")
	parser.add_argument("--outputTrain", type=str, default="",
						help="The path of the output test folder in which .txt annotations will be saved.")
	parser.add_argument("--outputTest", type=str, default="",
						help="The path of the output test folder in which .txt annotations will be saved.")
	return parser.parse_args()


def check_arguments_errors(args: argparse.Namespace) -> None:
	if not os.path.exists(args.inputAnno):
		raise (ValueError(f"Invalid input folder path: {os.path.abspath(args.inputAnno)}"))
	if not os.path.exists(args.inputTrain):
		raise (ValueError(f"Invalid input folder path: {os.path.abspath(args.inputTrain)}"))
	if not os.path.exists(args.inputTest):
		raise (ValueError(f"Invalid input folder path: {os.path.abspath(args.inputTest)}"))
	if not os.path.exists(args.outputTrain):
		raise (ValueError(f"Invalid input folder path: {os.path.abspath(args.outputTrain)}"))
	if not os.path.exists(args.outputTest):
		raise (ValueError(f"Invalid input folder path: {os.path.abspath(args.outputTest)}"))


def main() -> None:
	args = parser()
	check_arguments_errors(args)
	split_train_test(args.inputAnno, args.inputTrain, args.inputTest, args.outputTrain, args.outputTest)

	for label_path in ['train_labels', 'test_labels']:
		image_path = os.path.join(os.getcwd(), label_path)
		xml_df, classes = xml_to_csv(image_path)
		xml_df.to_csv(f'{label_path}.csv', index=None)
		print(f'Successfully converted {label_path} xml to csv.')

	label_map_path = os.path.join(os.getcwd(), "label_map.pbtxt")
	pbtxt_content = ""

	for i, class_name in enumerate(classes):
		pbtxt_content = (
				pbtxt_content
				+ "item {{\n    id: {0}\n    name: '{1}'\n}}\n\n".format(i + 1, class_name)
		)
	pbtxt_content = pbtxt_content.strip()
	with open(label_map_path, "w") as f:
		f.write(pbtxt_content)


if __name__ == "__main__":
	main()
import os
import cv2
import shutil

currentNumber = 481

# Path
path = "F:\Phan mem\Hoc Tap\May Hoc\AnhData2"
pathDes = "F:\Phan mem\Hoc Tap\May Hoc\ResultData"
length = 120

for filename in os.listdir(path):
	name = filename.split('.')[0]
	format = filename.split('.')[-1]
	name = name.split('_')[-1]
	black = name.split(' ')[0]

	if black == "black":
		img = cv2.imread(os.path.join(path, filename))
		crop_img = img[120:2040,:].copy()

		cv2.imwrite(os.path.join(pathDes, filename), crop_img)
	else:
		shutil.copyfile(os.path.join(path, filename), os.path.join(pathDes, filename))


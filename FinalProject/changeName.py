import shelve
import os
import shutil

currentNumber = 860
hashTable = shelve.open("hashTable")

# Path
pathOutside = "F:\Phan mem\Hoc Tap\May Hoc\ResultData"
pathInside = "F:\Phan mem\Hoc Tap\May Hoc\CS114.L21.KHCL\FinalProject\Data\DataRaw\Inside"
pathDestination = "F:\Phan mem\Hoc Tap\May Hoc\ResultData2"

outside = "outside"
inside = "inside"

for filename in os.listdir(pathOutside):
	if filename not in hashTable:
		name = filename.split('.')[0]
		format = filename.split('.')[-1]
		name = name.split('_')[-1]
		weather = name.split(' ')[0]

		newFileName = pathDestination + '/' + str(currentNumber) + '_' + weather + '_' + outside + '.' + format
		shutil.copyfile(pathOutside + '/' + filename, newFileName)
		hashTable[filename] = currentNumber

		currentNumber += 1


hashTable.close()



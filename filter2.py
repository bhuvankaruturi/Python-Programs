import re

def RemoveDuplicates(matches):
	uniqueList = []
	duplicate = False
	for i in range(0, len(matches)):
		for j in range(0, len(uniqueList)):
			if matches[i] == uniqueList[j]:
				duplicate = True
		if not duplicate:
			uniqueList.append(matches[i])
		duplicate = False
	return uniqueList

def ReplaceStrings(uniqueList, source, target):
	for i in range(0, len(uniqueList)):
		uniqueList[i] = str(uniqueList[i]).replace(source, target)
	return uniqueList

def WriteToFile(uniqueList, target, extension):
	try:
		fileToWrite = open('finalist-' + target + extension, 'w')
		for value in uniqueList:
			fileToWrite.writelines(value + '\n')
		fileToWrite.close()
	except(e):
		print("something went wrong while writing to the file" + "\n" + e)

text = ''
filename = input('enter filename: ')
source = input('string to be replaced: ')
target = input('string to be substituted: ')
extension = input('output file extension: ')

try:
	file = open(filename, 'r')
	text = file.read()
	file.close()
except:
	print('Something went wrong')

regExpression = "CREATE VIEW [\w]* "

matches = re.findall(regExpression, text)

if matches:
	WriteToFile(ReplaceStrings(RemoveDuplicates(matches), source, target), target, extension)
else:
	print('no matches')
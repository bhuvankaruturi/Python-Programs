import re

def removeDuplicatesAndPrint(matches):
    finalList = []
    duplicate = False
    for i in range(0, len(matches)):
        for j in range(0, len(finalList)):
            if matches[i] == finalList[j]:
                duplicate = True
                break
        if not duplicate:
            finalList.append(matches[i])
        duplicate = False
    finalList.sort()
    try:
        file2 = open('SQLs_Of_' + filename, 'w')
        for index, sql in enumerate(finalList):
            file2.writelines(str(index + 1) + ' - ' + sql[0:len(sql)-1] + '\n')
        file2.close()
        print('SQLs_Of_' + filename + ' file generated')
    except(e):
        print('something went wrong while writing to file' + '\n' + e)

filename = input('enter the filename: ')
text = ''
try:
    file1 = open(filename, 'r')
    text = file1.read()
    file1.close()
except:
    print('something went wrong')

matches = re.findall('SQL' + re.escape('.') + '\w*[,)]', text)
if matches:
    removeDuplicatesAndPrint(matches)
else:
    print('No Matches')
    


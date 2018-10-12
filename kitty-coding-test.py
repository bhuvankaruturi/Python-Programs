import string
alphaList = list(string.ascii_lowercase)

def isPalindrome(string):
	palindrome = True
	strLen = len(string) - 1
	for i in range(0, len(string)):
		if (string[i] != string[strLen-i]):
			palindrome = False
			return palindrome
	return palindrome	

count = 0
nonDecryptedList = []

#number of inputs
N = int(input())

#loop and process each input string
while N > 0:
	N -= 1
	encryptedString = input()
	decryptedString = ''
	for i in range(0, len(encryptedString)):
		letterIndex = alphaList.index(encryptedString[i])
		decryptedString += alphaList[letterIndex - i]
	if not isPalindrome(decryptedString):
		count += 1
		nonDecryptedList.append(decryptedString)

print(count)
for i in range(0, len(nonDecryptedList)):
	print(nonDecryptedList[i])


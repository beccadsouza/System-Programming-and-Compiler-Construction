
def is_palindrome(string):
	length = 0
	for x in string:
		length += 1
	for i in range(length/2):
		if string[i] != string[length-i-1]:
			return False
	return True

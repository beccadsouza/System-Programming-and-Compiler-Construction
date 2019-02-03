from palindrome_reb import is_palindrome
from substring_reb import is_substring

print("\nPress 1 for palindrome check\nPress 2 for substring check\nPress 3 to exit")
n = input()

while n!= 3:

	if n==1:
		print("Enter string to be checked")
		string = raw_input()
		print(is_palindrome(string))
		
	if n==2:
		print("Enter pattern to be searched")
		string1 = raw_input()
		print("Enter string in which pattern is to be detected")
		string2 = raw_input()
		print(is_substring(string1,string2))
	
	print("\nPress 1 for palindrome check\nPress 2 for substring check\nPress 3 to exit")
	n = input()
	

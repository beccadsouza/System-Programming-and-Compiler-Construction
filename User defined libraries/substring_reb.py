
def is_substring(string1,string2):

	length1 = 0
	length2 = 0
	
	for x in string1:
		length1 += 1
	for x in string2:
		length2 += 1
		
	if length1>length2: return False
	
	for i in range(0,length2-length1+1):
		if string2[i] == string1[0]:
			for k in range(0,length1):
				if string2[i+k]!=string1[k]:
					break
			return True
	return False
	
	


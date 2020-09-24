'''
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
'''
def len_cmp(str1,str2):
	t1=type(str1)
	t2=type(str2)
	len1=len(str1)
	len2=len(str2)
	if len1 > len2:
		 return str1
	elif len1 < len2:
		return str2
	if len1==len2:
		return str1,str2


str1=input()
str2=input()
answer=len_cmp(str1,str2)
print(answer)
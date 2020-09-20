str1="abcddkfk 123 kkjkjks12233 kjajsj 19989"
s1=""
list=[]
print(str1)
for char in str1:
	if char.isdigit():
		nextdigit=1
		if nextdigit==1:
			s1+=char
		else:
			list.append(s1)
	else:
		nextdigit=0
print(s1)
print(list)

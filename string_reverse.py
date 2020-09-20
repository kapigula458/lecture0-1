def reverse(string1):
	stringnew=""
	j=0
	for i in range(1,len(string1)+1):
		j=string1[-i]
		stringnew+=j
	return stringnew

new=reverse("abcdefghijklmon")
print("abcdefghijklmon",new)

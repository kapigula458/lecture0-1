'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

def sort_word(str1):
	list1=str1.split(",")
	list1.sort()
	return ','.join(list1)

answer=sort_word(input())
print(answer)
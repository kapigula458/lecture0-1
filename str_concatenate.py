'''
Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.
'''
def string_concat(str1,str2):
	return str1+str2


s1=input("enter the number1 ")
s2=input("Enter the number2 ")

answer=string_concat(s1,s2)
print("Concat the numbers in string s",answer)
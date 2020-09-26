'''
Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.
'''
def sum_strings_convert(str1,str2):
	s1=int(str1)
	s2=int(str2)
	sum=s1+s2
	return sum

num1=input("Enter any number ")
num2=input("Enter any number again ")

answer=sum_strings_convert(num1,num2)
print("sum of two numbers input as a string ",answer)
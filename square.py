'''
Question:
    Write a method which can calculate square value of number

Hints:
    Using the ** operator
'''
import math
def square(number):
	#num=int(number)
	sqr=number ** 2
	return sqr

answer=square(int(input("enter the number\n")))
print("the square is",answer)
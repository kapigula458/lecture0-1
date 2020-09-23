'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
j=input()

#a+aa+aaaa+aaaa

num2=j+j
num3=num2+j
num4=num3+j

answer=int(j)+int(num2)+int(num3)+int(num4)

print(answer)
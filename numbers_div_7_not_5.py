'''class get_print():

	def __init__(self):
		self.s=""

	def getString(self):
		self.s=input()

	def printString(self):
		print(self.s.upper())


strobject=get_print()
strobject.getString()
strobject.printString()

for i in range(2000,3201):
	j=i%7
	if j==0:
		k=i%5
		if k!=0:
			print("number divisible by 7 and not multiple of 5 is",i)


j=input("enter the number")
l1=j.split(",")
print(l1)
print(tuple(l1))


j=input()
ucnt=0
lcnt=0
for char in j:
	if char.isupper():
		ucnt+=1
	elif char.islower():
		lcnt+=1

print("upper case letter",ucnt)
print("lower case letter",lcnt)
'''

val=input("enter the list of any numbers sep by comma and it will return the odd numbers\n")
numbers=[x for x in val.split(",") if int(x)%2!=0]
print(",".join(numbers))
import random

def password(length):
	pw = str() # created a variable pw with string type
	characters="abcdefghijk" + "0123456789" + "!@#$%"

	for i in range(length):
		pw=pw+random.choice(characters)

	return pw

pwd = password(50)

print(pwd)




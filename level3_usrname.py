'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that
match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''



def validate_password(password):

	if len(password)<6 or len(password)>12:
		print("incorrect password provided length should be Minimum 6 or Maximum 12")
		exit()
	check1=0
	check2=0
	check3=0
	check4=0
	list=["@","$","#"]
	for char in password:
		if char.isdigit() and check1==0:
			check1=1
			#print("check1 success")
		if char.isupper() and check2==0:
			check2=1
			#print("check2 success")
		if char.isalpha() and check3==0:
			check3=1
			#print("check3 success")
		if char in list:
			check4=1

	if check3==1 and check2==1 and check1==1 and check4==1:
		print("All check done")
	elif check4==0:
		print("At least 1 character from [$#@] is not entered")
	elif check3==0:
		print(" At least 1 letter between [A-Z][a-z] is not entered")
	elif check2==0:
		print(" At least 1 letter should be in upper case")
	elif check1==0:
		print(" At least 1 letter should be digit")

password=input("Enter the password to register\n")

validate_password(password)
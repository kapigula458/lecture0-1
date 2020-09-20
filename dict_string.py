import string

mystring='''Thank you for giving the opportunity to apply.

I worked with Juniper, Tellabs, Altran(For Client Cisco), Gemalto organization ranging from small enterprise to larger one. Worked as a quality assurance in Juniper networks where my role involves validate the firewall features like IPSec VPN, digital certificate and routing.

Automation of regression and functional test using ROBOT test framework and Python. Intensively used Linux OS as part to run the 3rd party software open software for validating the solution.

Apart from QA I was responsible for customers issues related to SRX with clients like Ericsson, AT&T and many others. 

Worked as a mentor in Juniper and Cisco for technically bringing new candidates in training and development of the required skills set in our team
.
Presentation of new features to internal and external teams were part of culture to grow as an individual.'''

print(mystring)
print("========================================================================")
countofwords={}

mystring=mystring.replace(",","")
mystring=mystring.replace(".","")
mystring=mystring.lower()
mystring=mystring.split()
print(mystring)
for word in mystring:
	if word in countofwords.keys():
		countofwords[word]+=1
	else:
		countofwords[word]=1

print(countofwords)
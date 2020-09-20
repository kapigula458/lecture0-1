import time
import re

start=time.time()

def get_ip_address(input_str):
	str2=input_str.replace("\n"," ")
	lst=str2.split(" ")
	lst2=[]
	for val in lst:
		if re.findall(r"\d{1,3}.+\d{1,3}.+\d{1,3}.+\d{1,3}",val):
			lst2.append(val)
	return lst2

string1='''the loopback ip. addres of kapil machine is 127.0.0.1
he loopback ip addres of kapil machine. is 7.0.0.1 and
he loopback ip addres of kapil machine. is 157.0.0.1
he loopback ip addres of kapil machine is 16.0.0.1
'''
ipadd=get_ip_address(string1) 
print('the string is->','\n',string1,'\n','it contains an ip address->',ipadd)
stop=time.time()

totaltime=stop - start
print('total time to execute the code',totaltime,'ms')

#import numpy as np
import re

def convert_netmask(netmask):
	value = netmask.split(".")
	cnt=0
	for a in value:
			strg_int = int(a)
			int_bin = bin(strg_int)
			msk = re.findall(r'1*',int_bin)
			for a in msk:
				if a != '':
					cnt+=len(a)
	print("the netmask of",netmask,"=",cnt)

convert_netmask("255.255.255.0")






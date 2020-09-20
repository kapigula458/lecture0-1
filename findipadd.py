import re

def find_ip(input_str):
	search=re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',input_str)
find_ip("check 1.1.1.1")


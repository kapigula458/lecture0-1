'''
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
'''
def dict_sqr(num):
	dict1=dict()
	for i in range(1,num+1):
		dict1[i]=i**2
	return dict1

dict2=dict_sqr(20)
#if we want to print value from dict we can use dict1.items()

for (k,v) in dict2.items():
	print(v)

#BUt if we have to print key from dict we can just dict2.keys() or dict2.values()

for k in dict2.keys():
	print(k)

for v in dict2.values():
	print(v)

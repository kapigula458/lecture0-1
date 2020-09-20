import string
import numpy as py


def intersect(s1, s2):
	res=[]
	for x in s1:
		if x in s2:
			res.append(x)
	return res

def union(s1, s2):
	res=s1
	for y in s2:
		if y in res:
			pass
		else:res.append(y)
	return res



print("union",union(["adam","eve","John"],["adam","steve","eve","gary"]))
print("intersect",intersect([1,2,3,4],[3,4,5,6]))



		


def intersect(s1, s2):
	res=[]
	for x in s1:
		if x in s2:
			res.append(x)

	return res

news = intersect([1,2,3,4,5],[4,5,6,7,8])

print(news)

def swap(a,b):
	a=a+b
	b=a-b
	a=a-b
	print(a,b)

swap(4,5)

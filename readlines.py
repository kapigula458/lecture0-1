f=open("filenew.txt","a")
l1=["london","paris","NY","Utah"]

for l in l1:
	f.write(l +"\n ")

f.close()

f=open("filenew.txt","r")

newfile=f.readlines()[-5:]
print(newfile)
f.close()

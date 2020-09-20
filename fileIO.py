var1=3
var2=34
var3=112

newfile=open("storedata.txt","w")

newfile.write(str(var1)+"\n")
newfile.write(str(var2)+"\n")
newfile.write(str(var3)+"\n")

newfile.close()

s1=["david","John","sara","michael","lucy","Brian"]
newfile=open("dostoredata.txt","w")

for name in s1:
	newfile.write(name+"\n")

newfile.close()


s1=["david","John","sara","michael","lucy","Brian"]
newfile=open("usestoredata.txt","w")

newfile.writelines(s1)

newfile.close()

s1=["david","John","sara","michael","lucy","Brian"]
newfile=open("dousestoredata.txt","w")

newfile.write("\n".join(s1))

newfile.close()

s1=["david","John","sara","michael","lucy","Brian"]
newfile=open("1usestoredata.txt","w")

for name in s1:
	print(name, file = newfile)

newfile.close()



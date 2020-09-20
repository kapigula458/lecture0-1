import string
 
snt1="Jim quickly realized that the beautiful gowns are very expensive "
snt="Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth"
cmp=str()
newdict={}
for i in range(len(snt)):
	cmp=snt[i]
	cnt=0
	for char in snt:
		if cmp == char:
			cnt+=1
			newdict[char]=cnt

print(newdict)
print(newdict["h"])

L1=newdict.values()
for i in range(len(L1)):
		for j in range(len(L1)):
			if L1[j]>L1[i]:
				print("maximum value of the list is",L1[j])






	


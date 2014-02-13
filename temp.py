from main import *
f1 = open('uni.txt','w')
f2 = open('bi.txt','w')
p = len(pos_tags)
mat1 = np.zeros((p,m+2), dtype= int)
mat2 = np.zeros((p*p,m+2), dtype= int)
for i in range(len(train_data)):
	print i
	x = train_data[i]
	pos = train_POS[i]
	Y = y2int(train_labels[i])
	for j in range(len(pos)-1):
		cur = pos_tags.index(pos[j]) if (pos[j] in  pos_tags) else 0
		nxt = pos_tags.index(pos[j]) if (pos[j] in  pos_tags) else 0
		idx = nxt*p+ cur
		mat2[idx,Y[j+1]]+=1
		mat1[cur,Y[j+1]]+=1

f2.write("\t \t \t \t ")
f1.write("\t \t \t")
for i in range(m+2):
	f2.write(i2t(i)[:5]+"\t \t")
	f1.write(i2t(i)[:5]+"\t \t \t")
for i in range(p):
	f1.write('\n'+pos_tags[i]+"\t \t")
	for j in range(m+2):
		f1.write('\t \t '+str(mat1[i,j])+"\t")
	
	
for i in range(p*p):
	pt = pos_tags[i%p]
	ct = pos_tags[i/p]
	f2.write('\n'+pt + " "+ct+"\t")
	for j in range(m+2):
		f2.write('\t \t'+str(mat2[i,j])+"\t")
print np.count_nonzero(mat2)
print mat2.shape
f1.close()
f2.close()
	

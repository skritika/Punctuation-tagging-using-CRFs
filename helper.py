import numpy as np
from feature_templates import *
 # assume 0th tag = START, (m+1)th tag = STOP

def load_data(file_path):
    f = open('punctuationDataset/'+file_path+'.txt', 'r')
    list_data = [s.split() for s in f]
    return list_data

def f_matrix(X,Y):
	n = len(X[0])
	ret = np.zeros((J,n+2),dtype=float) #(:,0) not used
	for i in range(1,n+2):	
		temp = f(Y[i-1],Y[i],X,i)
		for j in temp: 
			ret[j,i] = 1.0		
	return ret
	
def F(X, Y, W):
	return  np.sum(f_matrix(X,Y), axis =1)

def g(i,y_1,y,X,W):
    ret = 0.0
    nz_b =[]
    temp = f(y_1,y,X,i)
    for j in temp:
		ret += W[j]
    return ret

def g_vector(i,v,X,W, method): #g customised for alpha,beta calculation
    ret = np.empty(m+2,dtype=float)
    if(method == "alpha"):		
        for u in range(m+2):
            ret[u] = g(i,u,v,X,W) 
    elif(method=="beta"):
        for u in range(m+2):
            ret[u] = g(i,v,u,X,W)
    return ret

def alpha(X,W):
	n = len(X[0])
	a = np.zeros((n+1,m+2),dtype=float)
	a[0,0]=1.0
	for k in range(n):
		for v in range(m+2):
			a[k+1,v] = np.dot(a[k,:], np.exp(g_vector(k+1,v,X,W,"alpha")))
	return a

def beta(X,W):
    n = len(X[0])
    b = np.zeros((m+2,n+2),dtype=float)
    b[m+1,n+1] = 1.0
    for k in range(n,0,-1):
        for u in range(m+2):
            b[u,k] = np.dot(b[:,k+1].T, np.exp(g_vector(k+1,u,X,W,"beta")))
    return b

def Z(X,W,method):
	n = len(X[0])
	if(method=="alpha"):
		a = alpha (X,W)
		return sum(a[-1,:])
	elif(method=="beta") :
		b = beta(X, W)
		return np.dot(np.exp(g_vector(1,0,X,W,"beta")), b[:,1])
	
def expectation_F(X,W):
	F = np.zeros(J, dtype=float)
	n = len(X[0])
	a = alpha(X,W)
	b = beta(X,W)
	z = sum(a[-1,:])
	for j in range(J):
		for i in range(1,n+1):
			for l in range(0,m+1):
				for k in range(1,m+2):
					F[j] = F[j] + f(j,l,k,X,i)*(a[i-1,l]*np.exp(g(i,l,k,X,W))* b[k,i])
	return F/z

def gibbs(X,Y,W,num):
	n = len(X[0])
	g1 = np.zeros((n+2,m+2),dtype=float)	#gi(yi_1,v)
	for i in range(1,n+2):
		g1[i,:] = g_vector(i,Y[i-1],X,W,"beta")		

	g2 = np.zeros((n+2,m+2),dtype=float)	#gi+1(v,yi+1)
	for i in range(2,n+2):
		g2[i,:] = g_vector(i,Y[i],X,W,"alpha")		
	Y_new = np.zeros(n+2)
	Y_new[0] = 0
	Y_new[n+1] = 7
	distri = np.zeros(m+2,dtype=float)
	for i in range(1,n+1):
		for j in range(1,m+1):
			distri[j] = np.exp(g1[i,j])*np.exp(g2[i+1,j])
		distri = distri/np.sum(distri)
		try:
			Y_new[i] = int(np.random.choice(len(distri),1,p=distri))
		except:
			print distri
			print sum(distri)
	return Y_new		

def sga_grad(X,Y,W):
	return (F(X, Y, W) - expectation_F(X, W))

def collins_grad(X,Y,W):
	return (F(X, Y, W) - F(X,decode(X,W), W))

def contrdiv_grad(X,Y,W):
	Y_new = gibbs(X,Y,W,1)
	#print "alp" , Z(X,W,"alpha",nz_a), "bet", Z(X,W,"beta",nz_a)
	return (F(X, Y, W) - F(X, Y_new, W))

def decode(X,W):
	n = len(X[0])
	U = np.empty((n+1,m+2),dtype=float) #U[0,:] not used 
	y_hat = np.zeros(n+2,dtype=int) # y_hat[0] not used
	y_hat[n+1] = m+1 #stop tag
	## filling U matrix
	for v in range(m+2):
		U[1,v] = g(1,t2i("START"),v,X,W)
	for k in range(2,n+1):
		for v in range(m+2):
			U[k,v] = np.max(U[k-1,:] + g_vector(k,v,X,W,"alpha"))
	## finding optimal sequence
	y_hat[n] = 	argmax(U[n,:])
	for i in range(n-1,0,-1):
		y_hat[i] = argmax(U[i,:] + g_vector(i+1,y_hat[i+1],X,W,"alpha"))
	return y_hat

def argmax(v):
	if(v[0]==v[1] and v[1]==v[2]):
		print "same"
	return np.argmax(v[1:-1])+1
	
def y2int(Y): #start and stop tags appended
	n = len(Y)
	tags = np.empty(n+2, dtype=int)
	tags[0] = 0
	tags[n+1] = m+1
	for i in range(n):
		tags[i+1] = t2i(Y[i])
	return tags

def y2tag(Y): #start and stop tags ignored
	tags = []
	for i in range(1,len(Y)):
		tags.append(i2t(Y[i]))
	return tags


def POS(sentence):
    pos = nltk.pos_tag(sentence)
    tags = []
    for each in pos:
        tags.append(each[1])
    return tags

def non_zero_a(X):
	n = len(X[0])
	nz_a = [[]]
	cur = []
	for i in range(1,n+2):
		for k in range(num_a):
			if(a(k,X,i)): cur.append(k)
		nz_a.append(cur)
		cur=[]
	#print max([len(j) for j in [[1,2],[]] ])
	return nz_a

def non_zero_b(X): #do it later
	nz_b = [[]]
	for i in range(1,n+1):
		cur = []
		for k in range(num_b):
			if(b(k,X)): cur.append(k)
		nz_a.append(cur)
	
	return nz_a

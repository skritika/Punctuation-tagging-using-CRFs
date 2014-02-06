import numpy as np
from feature_functions import *
global m
m = 6 # assume 0th tag = START, (m+1)th tag = STOP

def load_data(file_path):
    f = open(file_path, 'r')
    list_data = [s.split() for s in f]
    return list_data

def F(X, Y, W):
	n = len(X)
	F_vec = np.zeros(J, dtype=float)
	for j in range(J):	
		for i in range(1,n+2):
			F_vec[j] += f(j,Y[i-1],Y[i],X,i)
	return F_vec

def g(i,y_1,y,X,W):
    ret = 0.0
    for j in range(J):
        ret += W[j] * f(j,y_1,y,X,i) 
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
	n = len(X)
	a = np.zeros((n+1,m+2),dtype=float)
	a[0,0]=1.0
	for k in range(n):
		for v in range(m+2):
			a[k+1,v] = np.dot(a[k,:], np.exp(g_vector(k+1,v,X,W,"alpha")))
	return a

def beta(X,W):
    n = len(X)
    b = np.zeros((m+2,n+2),dtype=float)
    b[m+1,n+1] = 1.0
    for k in range(n,0,-1):
        for u in range(m+2):
            b[u,k] = np.dot(b[:,k+1].T, np.exp(g_vector(k+1,u,X,W,"beta")))
    return b

def Z(X,W,method):
	n = len(X)
	if(method=="alpha"):
		a = alpha (X,W)
		return sum(a[-1,:])
	elif(method=="beta") :
		b = beta(X,W)
		return np.dot(np.exp(g_vector(1,0,X,W,"beta")), b[:,1])
	
def expectation_F(X,W):
	F = np.zeros(J, dtype=float)
	n = len(X)
	a = alpha(X,W)
	b = beta(X,W)
	z = sum(a[-1,:])
	for j in range(J):
		for i in range(1,n+1):
			for l in range(0,m+1):
				for k in range(1,m+2):
					F[j] = F[j] + f(j,l,k,X,i)*(a[i-1,l]*np.exp(g(i,l,k,X,W))* b[k,i])
	return F/z

def sga_grad(X,Y,W):
	return (F(X, Y, W) - expectation_F(X,W))

def collins_grad(X,Y,W):
	return (F(X, Y, W) - F(X,decode(X,W),W))

def decode(X,W):
	n = len(X)
	U = np.empty((n+1,m+2),dtype=float) #U[0,:] not used 
	y_hat = np.zeros(n+2,dtype=int) # y_hat[0] not used
	y_hat[n+1] = m+1 #stop tag
	## filling U matrix
	for v in range(m+2):
		U[1,v] = g(1,t2i("START"),v,X,W)
	for k in range(2,n+1):
		for v in range(m+2):
			U[k,v] = np.max(U[k-1,:]+g_vector(k,v,X,W,"alpha"))
	## finding optimal sequence
	y_hat[n] = 	np.argmax(U[n,:])
	for i in range(n-1,0,-1):
		y_hat[i] = np.argmax(U[i,:]+g_vector(i+1,y_hat[i+1],X,W,"alpha"))
	return y_hat

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

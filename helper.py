import numpy as np
import nltk.tag
from feature_functions import *
global m
m = 6 # assume 0th tag = START, (m+1)th tag = STOP

def load_data(file_path):
    f = open(file_path, 'r')
    list_data = f.readlines()
    return list_data

def POS(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos = nltk.pos_tag(tokens)
    tags = []
    for each in pos:
        tags.append(each[1])
    return tags

def F(j, X, Y, W):
	n = len(X)
	ret = 0.0
	for i in range(1,n+1):
		ret += f(j,Y[i-1],Y[i],X,i)
	return ret

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
		return sum(a[n,:])
	elif(method=="beta") :
		b = beta(X,W)
		return np.dot(np.exp(g_vector(1,0,X,W,"beta")), b[:,1])
	
def expectation_F(j,W,X):
	n = len(X)
	val = 0.0
	a = alpha(X,W)
	b = beta(X,W)
	z = sum(a[n,:])
	for i in range(0,n):
		for l in range(0,m+2):
			for k in range(1,m+2):
			    val = val + f(j,l,k,X,i)*(a(i-1,l)*np.exp(g(i,l,k,X,W))* b[k,i])/z
	return val

def single_grad(j,X,W,Y):
	ret = np.empty(J,dtype=float)
	for j in range(J):
		ret[j] =  (F(j, X, Y, W) - expectation_F(j,W,X))
	return ret

def decode(X,W):
	n = len(X)
	U = np.empty((n+1,m+2),dtype=float) #U[0,:] not used 
	y_hat = np.zeros(n+1,dtype=int) # y_hat[0] not used
	
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

def y2int(Y):
	tags = np.empty(len(Y), dtype=int)
	for i in range(len(Y)):
		tags[i] = t2i(Y[i])
	return tags

def y2tag(Y):
	tags = []
	for i in range(len(Y)):
		tags.append(i2t(Y[i]))
	return tags
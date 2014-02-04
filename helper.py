import nltk.tag
from feature_functions import *
global J,m
J = 5 # no. of feature function used
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
    ret = np.zeros(m+2,dtype=float)
    if(method == "alpha"):		
        for u in range(m+2):
            ret[u] = g(i,u,v,X,W) 
    elif(method=="beta"):
        for u in range(m+2):
            ret[u] = g(i,v,u,X,W)
    return ret

def alpha(X,W):
	a = np.zeros((n+1,m+2),dtype=float)
	a[0,0]=1.0
	for k in range(n):
		for v in range(m+2):
			a[k+1,v] = np.dot(alpha[k,:], np.exp(g_vector(k+1,v,X,W,"alpha")))
	return a

def beta(X,W):
    b = np.zeros((m+2,n+2),dtype=float)
    b[m+1,n+1] = 1.0
    for k in range(n,0,-1):
        for u in range(m+2):
            b[u,k] = np.dot(b[:,k+1], np.exp(g_vector(k+1,u,X,W,"beta")))
    return b

def Z(X,W,method):
	n = len(X)
	if(method=="alpha"):
		a = alpha (X,W)
		return sum(a[n,:])
	elif(method=="beta") :
		b = beta(X,W)
		return np.dot(np.exp(g_vector(0,0,X,W,"beta")), b[:,0])
	
def expectation_F(j,X,Y):
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

def t2i (tag): #tag to int
	if(tag=="START"): return 0
	elif(tag=="COMMA"): return 1
	elif(tag=="PERIOD"): return 2
	elif(tag=="QUESTION_MARK"): return 3
	elif(tag=="EXCLAMATION_POINT"): return 4
	elif(tag=="COLON"): return 5
	elif(tag=="SPACE"): return 6
	elif(tag=="STOP"): return 7
	else: return -1

def i2t (val): # int to tag
	if(val==0): return "START"
	elif(val==1): return "COMMA"
	elif(val==2): return "PERIOD"
	elif(val==3): return "QUESTION_MARK"
	elif(val==4): return "EXCLAMATION_POINT"
	elif(val==5): return "COLON"
	elif(val==6): return "SPACE"
	elif(val==7): return "STOP"
	else: return ""

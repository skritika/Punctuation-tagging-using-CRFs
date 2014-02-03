import nltk.tag
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
    return 0

def f(j,y_1,y,X,i):
    return 0

def g(i,y_1,y,X,W):
    ret = 0.0
    for j in range(J):
        ret += W[j] * f(j,y_1,y,X,i) 
    return ret

def g_vector(i,y,X,W, method): #g customised for alpha,bet calculation
    ret = np.zeros(m+2,dtype=float)
    if(method == "alpha"):		
        for x in range(m+2):
            ret[x] = g(j,x,y,X,W) 
    elif(method=="beta"):
        for x in range(m+2):
            ret[x] = g(j,y,x,X,W) 
    return ret

def alpha(X,W):
	a = np.zeros((n+1,m+2),dtype=float)
	a[0,0]=1.0
	for k in range(0,n):
		for v in range(0,m):
			a[k+1,v] = np.dot(alpha[k,:], np.exp(g_vector(k,v,X,W,"alpha")))
	return a

def beta(X,W):
    b = np.zeros((m+2,n+1),dtype=float)
    b[m+1,n] = 1.0
    for k in range(n-1,0,-1):
        for u in range(0,m+2):
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

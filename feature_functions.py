'''
1. The current word is 'and, but, yet, or, nor, for, so' and the previous tag is COMMA. 
2. The current word is 'however, consequently, otherwise, moreover, nevertheless', the previous tag is COMMA and the current tag is COMMA.
3. The previous tag is 'PERIOD/EXCLAMATION_POINT/QUESTION_MARK' and the current tag is STOP.
4. The previous tag is START, the current word is 'well, now, yes, moreover, furthermore, specifically, however, likewise, therefore, consequently, meanwhile'(transitional phrase) and the current tag is COMMA. Basically transitional phrase at the beginning of a sentence.

Using POS
'''

import nltk
global num_a, num_b, J
num_a = 22
num_b = 7
J = num_a*num_b

def f(j, yi_1, yi, X, i):
	#j = ai + (bi-1)*num_a
	ai = j%num_a
	bi = (j-ai)/num_a + 1
	return a(ai, X, i) and b(bi, yi_1, yi, i)


def b1(yi_1, yi, i):
	return int(yi_1==t2i('COMMA'))
def b2(yi_1, yi, i):
	return int(yi_1==t2i('COMMA') and yi==t2i('COMMA'))
def b3(yi_1, yi, i):
	return int(yi_1==t2i('PERIOD') and yi==t2i('STOP'))
def b4(yi_1, yi, i):
	return int(yi_1==t2i('EXCLAMATION_POINT') and yi==t2i('STOP'))
def b5(yi_1, yi, i):
	return int(yi_1==t2i('QUESTION_MARK') and yi==t2i('STOP'))
def b6(yi_1, yi, i):
	return int(yi_1==t2i('START') and yi==t2i('COMMA'))
def b7(yi_1, yi, i):
	return int(yi_1==t2i('START') and yi==t2i('COLON'))

def b(n, yi_1, yi, i):
	arr_b = ['b1(yi_1, yi, i)','b2(yi_1, yi, i)','b3(yi_1, yi, i)','b4(yi_1, yi, i)','b5(yi_1, yi, i)','b6(yi_1, yi, i)','b7(yi_1, yi, i)']
 	a = exec(arr_b[n-1])
	return a

def a(n, X, i):
	length = len(X)
	if(i==len(X)+1):
		return 0
	i = i - 1
	if(n==1):
		return int(X[i].lower()=='and')
	elif(n==2):
		return int(X[i].lower()=='but')
	elif(n==3):
		return int(X[i].lower()=='yet')
	elif(n==4):
		return int(X[i].lower()=='or')
	elif(n==5):
		return int(X[i].lower()=='nor')
	elif(n==6):
		return int(X[i].lower()=='for')
	elif(n==7):
		return int(X[i].lower()=='so')
	elif(n==8):
		return int(X[i].lower()=='however')
	elif(n==9):
		return int(X[i].lower()=='consequently')
	elif(n==10):
		return int(X[i].lower()=='otherwise')
	elif(n==11):
		return int(X[i].lower()=='moreover')
	elif(n==12):
		return int(X[i].lower()=='nevertheless')
	elif(n==13):
		return int(X[i].lower()=='well')
	elif(n==14):
		return int(X[i].lower()=='now')
	elif(n==15):
		return int(X[i].lower()=='yes')
	elif(n==16):
		return int(X[i].lower()=='furthermore')
	elif(n==17):
		return int(X[i].lower()=='specifically')
	elif(n==18):
		return int(X[i].lower()=='likewise')
	elif(n==19):
		return int(X[i].lower()=='meanwhile')
	elif(n==20):	
		pos = POS(X)
		return int(pos[0]=='NNP')
	elif(n==21):
		return int(X[0].lower()=='the')
	elif(n==22):
		return int(X[0].lower()=='i')
	else :	
		print 'err! wrong n'
		return 0

def t2i(tag): #tag to int
	if(tag=="START"): return 0
	elif(tag=="COMMA"): return 1
	elif(tag=="PERIOD"): return 2
	elif(tag=="QUESTION_MARK"): return 3
	elif(tag=="EXCLAMATION_POINT"): return 4
	elif(tag=="COLON"): return 5
	elif(tag=="SPACE"): return 6
	elif(tag=="STOP"): return 7
	else: return -1

def i2t(val): # int to tag
	if(val==0): return "START"
	elif(val==1): return "COMMA"
	elif(val==2): return "PERIOD"
	elif(val==3): return "QUESTION_MARK"
	elif(val==4): return "EXCLAMATION_POINT"
	elif(val==5): return "COLON"
	elif(val==6): return "SPACE"
	elif(val==7): return "STOP"
	else: return ""


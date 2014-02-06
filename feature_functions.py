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


def b(n, yi_1, yi, i):
	return{
		1: int(yi_1==t2i('COMMA')),
		2: int(yi_1==t2i('COMMA') and yi==t2i('COMMA')),
		3: int(yi_1==t2i('PERIOD') and yi==t2i('STOP')),
		4: int(yi_1==t2i('EXCLAMATION_POINT') and yi==t2i('STOP')),
		5: int(yi_1==t2i('QUESTION_MARK') and yi==t2i('STOP')),
		6: int(yi_1==t2i('START') and yi==t2i('COMMA')),
		7: int(yi_1==t2i('START') and yi==t2i('COLON'))
	}[n]
	
def a(n, X, i):
	[x, p] = X
	length = len(x)
	if(i==len(x)+1):
		return 0
	i = i - 1
	if(n==1):
		return int(x[i].lower()=='and')
	elif(n==2):
		return int(x[i].lower()=='but')
	elif(n==3):
		return int(x[i].lower()=='yet')
	elif(n==4):
		return int(x[i].lower()=='or')
	elif(n==5):
		return int(x[i].lower()=='nor')
	elif(n==6):
		return int(x[i].lower()=='for')
	elif(n==7):
		return int(x[i].lower()=='so')
	elif(n==8):
		return int(x[i].lower()=='however')
	elif(n==9):
		return int(x[i].lower()=='consequently')
	elif(n==10):
		return int(x[i].lower()=='otherwise')
	elif(n==11):
		return int(x[i].lower()=='moreover')
	elif(n==12):
		return int(x[i].lower()=='nevertheless')
	elif(n==13):
		return int(x[i].lower()=='well')
	elif(n==14):
		return int(x[i].lower()=='now')
	elif(n==15):
		return int(x[i].lower()=='yes')
	elif(n==16):
		return int(x[i].lower()=='furthermore')
	elif(n==17):
		return int(x[i].lower()=='specifically')
	elif(n==18):
		return int(x[i].lower()=='likewise')
	elif(n==19):
		return int(x[i].lower()=='meanwhile')
	elif(n==20):	
		return int(i==0 and p[0]=='NNP')
	elif(n==21):
		return int(i==0 and x[0].lower()=='the')
	elif(n==22):
		return int(i==0 and x[0].lower()=='i')
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


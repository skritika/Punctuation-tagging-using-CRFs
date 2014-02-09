'''
1. The current word is 'and, but, yet, or, nor, for, so' and the previous tag is COMMA. 
2. The current word is 'however, consequently, otherwise, moreover, nevertheless', the previous tag is COMMA and the current tag is COMMA.
3. The previous tag is 'PERIOD/EXCLAMATION_POINT/QUESTION_MARK' and the current tag is STOP.
4. The previous tag is START, the current word is 'well, now, yes, moreover, furthermore, specifically, however, likewise, therefore, consequently, meanwhile'(transitional phrase) and the current tag is COMMA. Basically transitional phrase at the beginning of a sentence.

Using POS
'''

import nltk
global num_a, num_b, J
num_a = 9
num_b = 11
J = num_a*num_b

def f(j, yi_1, yi, X, i):
	#j = ai + bi*num_a
	ai = j%num_a
	bi = (j-ai)/num_a
	if (a(ai, X, i) and b(bi, yi_1, yi, i)):
		return 1.0
	else: return 0.0

def b(n, yi_1, yi, i):
	return{
		0: yi_1==t2i('START'),
		1: yi_1==t2i('COMMA'),
		2: yi_1==t2i('COMMA') and yi==t2i('COMMA'),
		3: yi_1==t2i('PERIOD') and yi==t2i('STOP'),
		4: yi_1==t2i('EXCLAMATION_POINT') and yi==t2i('STOP'),
		5: yi_1==t2i('QUESTION_MARK') and yi==t2i('STOP'),
		6: yi_1==t2i('START') and yi==t2i('COMMA'),
		7: yi_1==t2i('START') and yi==t2i('COLON'),
		8: yi==t2i('COMMA'),
		9: yi==t2i('SPACE'),
		10: yi_1==t2i('SPACE')
	}[n]
	
def a(n, X, i):
	[x, p] = X
	length = len(x)
	f = i<>(length+1)
	i = i - 1
	return {
		0: f and 1,
		1: f and x[i].lower()=='and',
		2: f and x[i].lower()=='but',
		3: f and x[i].lower()=='or',
		4: f and p[i]=='NNP',
		5: f and x[i].lower()=='however',
		6: f and x[i].lower()=='therefore',
		7: f and x[i].lower()=='consequently',
		8: x[0].lower() in ['were','have','can','was', 'who', 'what', 'why', 'where', 'do', 'is', 'whose', 'when', 'how','are']
	}[n]

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


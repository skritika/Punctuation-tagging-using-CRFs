'''
1. The current word is 'and, but, yet, or, nor, for, so' and the previous tag is COMMA. 
2. The current word is 'however, consequently, otherwise, moreover, nevertheless', the previous tag is COMMA and the current tag is COMMA.
3. The previous tag is 'PERIOD/EXCLAMATION_POINT/QUESTION_MARK' and the current tag is STOP.
4. The previous tag is START, the current word is 'well, now, yes, moreover, furthermore, specifically, however, likewise, therefore, consequently, meanwhile'(transitional phrase) and the current tag is COMMA. Basically transitional phrase at the beginning of a sentence.

Using POS
'''

import nltk
from copy import copy, deepcopy
global num_a, num_b, J, pos_tags, punc_tags, a_func, b_func
a_func = []
b_func = []
pos_tags = ["OTH", "CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNP","NNPS","NNS","PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","SYM","TO","UH","VB","VBD","VBG","VBN","VBP","VBZ","WDT","WP","WP$","WRB"]
punc_tags = ["START", "COMMA", "PERIOD", "QUESTION_MARK", "EXCLAMATION_POINT", "COLON",	"SPACE", "STOP"]
possible_bigrams = [[1,2,5,6],[1,2,3,4,6],[7],[7],[7],[1,2,6],[1,2,3,4,5,6],[]  ]
#################### b_function implementation
def same(p): return p
def b(n, yi_1, yi, i):
	return b_func[n](yi_1,yi,i)
p = 0
for p in range(len(punc_tags)):
	b_func.append(lambda yi_1,yi,i, p=p: yi==p)
	b_func.append(lambda yi_1,yi,i, p=p: yi_1==p)
	for q in possible_bigrams[p]:
		b_func.append(lambda yi_1,yi,i, p=p, q=q: yi_1==p and yi==q)

#b_func.append(lambda yi_1,yi,i: yi_1==t2i('START'))
#b_func.append(lambda yi_1,yi,i: yi_1==t2i('COMMA'))
#b_func.append(lambda yi_1,yi,i: yi_1==t2i('COMMA') and yi==t2i('COMMA'))
#b_func.append(lambda yi_1,yi,i: yi_1==t2i('PERIOD') and yi==t2i('STOP'))
#b_func.append(lambda yi_1,yi,i: yi_1==t2i('EXCLAMATION_POINT') and yi==t2i('STOP'))
#b_func.append(lambda yi_1,yi,i: yi_1==t2i('QUESTION_MARK') and yi==t2i('STOP'))
#b_func.append(lambda yi_1,yi,i: yi_1==t2i('START') and yi==t2i('COMMA'))
#b_func.append(lambda yi_1,yi,i: yi_1==t2i('START') and yi==t2i('COLON'))
#b_func.append(lambda yi_1,yi,i: yi==t2i('COMMA'))
#b_func.append(lambda yi_1,yi,i: yi==t2i('SPACE'))
#b_func.append(lambda yi_1,yi,i: yi==t2i('COLON'))

	
#################### a_function implementation
def a(n, X, i):
	[x, pos] = X
	length = len(x)
	f = i<(length)
	i = i - 1
	return a_func[n](x,pos,i,f)
	

for p in pos_tags:
	a_func.append(lambda x, pos, i, f, p=p: f and  pos[i]==p )
	#print a_func[0](["re","rfv"], ["CC","CC"], 0, True)
	for q in pos_tags:
		a_func.append(lambda x, pos, i, f, p=p, q=q: f and  (pos[i]==p and pos[i+1]==q))
a_func.append(lambda x, pos, i, f: i<len(x)-1 and  x[i+1][0].isupper())
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='but')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='and')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='or')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='however')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='therefore')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='therefore')
a_func.append(lambda x, pos, i, f: i==len(x)+1 and x[0].lower() in ['were','have','can','was', 'who', 'what', 'why', 'where', 'do', 'is', 'whose', 'when', 'how','are'])
a_func.append(lambda x, pos, i, f: f and i==0 and pos[0]=="RB")
a_func.append(lambda x, pos, i, f: f and x[i] in ["-","--"])

#############
num_a =  len(a_func)
num_b =  len(b_func)
J = num_a*num_b
print J
def f(j, yi_1, yi, X, i):
	#j = ai + bi*num_a
	ai = j%num_a
	bi = (j-ai)/num_a
	if (b(bi, yi_1, yi, i) and a(ai, X, i) ):
		return 1.0
	else: return 0.0

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


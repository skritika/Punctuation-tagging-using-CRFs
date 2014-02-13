'''
1. The current word is 'and, but, yet, or, nor, for, so' and the previous tag is COMMA. 
2. The current word is 'however, consequently, otherwise, moreover, nevertheless', the previous tag is COMMA and the current tag is COMMA.
3. The previous tag is 'PERIOD/EXCLAMATION_POINT/QUESTION_MARK' and the current tag is STOP.
4. The previous tag is START, the current word is 'well, now, yes, moreover, furthermore, specifically, however, likewise, therefore, consequently, meanwhile'(transitional phrase) and the current tag is COMMA. Basically transitional phrase at the beginning of a sentence.

Using POS
'''

import nltk
global num_a, num_b, J, pos_tags, punc_tags, t1, t2, t3, a_hoc, m
pos_tags = ["OTH", "CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNP","NNPS","NNS","PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","SYM","TO","UH","VB","VBD","VBG","VBN","VBP","VBZ","WDT","WP","WP$","WRB"]
punc_tags = ["START", "COMMA", "PERIOD", "QUESTION_MARK", "EXCLAMATION_POINT", "COLON",	"SPACE", "STOP"]
end_tags = ["PERIOD", "QUESTION_MARK", "EXCLAMATION_POINT"]
m=6

t1 = m+2
def template_1(offset, yi_1, yi, X, i):
	n = len(X[0])
	if(i==n):
		return [offset+yi]
	else:
		return []

t2=m+2
def template_2(offset, yi_1, yi, X, i):
	n = len(X[0])
	if(yi==t2i("STOP")):
		return [offset+yi_1]
	else:
		return []

t3= len(pos_tags)*len(pos_tags)*m
def template_3(offset, yi_1, yi, X, i):
	n = len(X[0])
	p = len(pos_tags)
	i-=1
	[x, pos]= X
	if(yi==t2i("STOP") or yi==t2i("START") or i==0 or i==n): return []
	else:
		pi = (pos_tags.index(pos[i-1])) if (pos[i-1] in pos_tags) else 0
		ci = (pos_tags.index(pos[i])) if (pos[i] in pos_tags) else 0
		return [offset+ ((yi-1)*p*p) + (pi*p) + (ci)]

t4=(m+2)*len(end_tags)
def template_4(offset, yi_1, yi, X, i):
	n = len(X[0])
	if(yi_1 in end_tags):
		return [offset+ end_tags.index(yi_1)*yi ]
	else:
		return []

t5= len(pos_tags)*(m+2)
def template_5(offset, yi_1, yi, X, i):
	n = len(X[0])
	p = len(pos_tags)
	i-=1
	[x, pos]= X
	if(i==0): 
		ci = (pos_tags.index(pos[i])) if (pos[i] in pos_tags) else 0
		return [offset+ yi*p + ci]
	else: return []

t6= len(pos_tags)*(m+2)
def template_6(offset, yi_1, yi, X, i):
	n = len(X[0])
	p = len(pos_tags)
	i-=1
	[x, pos]= X
	if(i==n-1): 
		ci = (pos_tags.index(pos[i])) if (pos[i] in pos_tags) else 0
		return [offset+ yi*p + ci]
	else: return []
	
a_hoc = 8*(m+2)
def ad_hoc(offset, yi_1, yi, X, i):
	n = len(X[0])
	[x, pos] = X
	ret = []
	f = (i<=n)
	i = i - 1
	if( f and  x[i].lower()=='but'): ret.append(offset + 1*yi_1)
	offset= offset + (m+2)
	if( f and  x[i].lower()=='however'): ret.append(offset + yi_1)
	offset= offset + (m+2)
	if( f and  x[i].lower()=='however'): ret.append(offset + yi)
	offset= offset + (m+2)
	if( i==len(x)-1 and x[0].lower() in ['were','have','can','was', 'who', 'what', 'why', 'where', 'do', 'is', 'whose', 'when', 'how','are']): ret.append(offset+ yi)
	offset= offset + (m+2)
	if( f and i==0 and pos[0]=="RB"): ret.append(offset + yi)
	offset= offset + (m+2)
	if( f and i==0 and pos[0].endswith('ly')): ret.append(offset + yi)
	offset= offset + (m+2)
	if( f and x[i] in ["-","--"]): ret.append(offset + yi)
	offset= offset + (m+2)
	if( i<len(x)-1 and  x[i+1][0].isupper()): ret.append(offset + yi)
	offset= offset + (m+2)
	return ret


J = t1 + t2 + t3 + t4 + t5 +  a_hoc
print J
def f(yi_1, yi, X, i):
	ret = template_1(0, yi_1, yi, X, i)
	ret+= template_2(t1, yi_1, yi, X, i)
	ret+= template_3(t2, yi_1, yi, X, i)
	ret+= template_4(t3, yi_1, yi, X, i)
	ret+= template_5(t4, yi_1, yi, X, i)
	ret+= template_6(t5, yi_1, yi, X, i)
	ret+= ad_hoc(t6, yi_1, yi, X, i)
	return ret

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


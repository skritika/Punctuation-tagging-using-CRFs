'''
1. The current word is 'and, but, yet, or, nor, for, so' and the previous tag is COMMA. 
2. The current word is 'however, consequently, otherwise, moreover, nevertheless', the previous tag is COMMA and the current tag is COMMA.
3. The previous tag is 'PERIOD/EXCLAMATION_POINT/QUESTION_MARK' and the current tag is STOP.
4. The previous tag is START, the current word is 'well, now, yes, moreover, furthermore, specifically, however, likewise, therefore, consequently, meanwhile'(transitional phrase) and the current tag is COMMA. Basically transitional phrase at the beginning of a sentence.

Using POS
'''

def b(n, y, i):
	if(n==1):
		return int(y[i-1]=='COMMA')
	elif(n==2):
		return int(y[i-1]=='COMMA' and y[i]=='COMMA')
	elif(n==3):
		return int(y[i-1]=='PERIOD' and y[i]=='STOP')
	elif(n==4):
		return int(y[i-1]=='EXCLAMATION_POINT' and y[i]=='STOP')
	elif(n==5):
		return int(y[i-1]=='QUESTION_MARK' and y[i]=='STOP')
	elif(n==6):
		return int(y[i-1]=='START' and y[i]='COMMA')
	else:
		print 'err! wrong n'
	

def a(n, x, i):
	length = len(x)
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
	elif(n==16):
		return int(x[i].lower()=='likewise')
	elif(n==16):
		return int(x[i].lower()=='meanwhile')
	else:
		print 'err! wrong n'

	



def f(j,y_1,y,X,i):
	n = len(X)
	if(j==1):# sentence ens with "."
		if(i==n and y==t2i("PERIOD")):	return 1
		
	elif(j==2):# sentence ens with "?"
		if(i==n and y==t2i("QUESTION_MARK")):	return 1
	
	elif(j==3):#sentence ends with "!"
		if(i==n and y=="EXCLAMATION_POINT"):	return 1
	
	elif(j==4): #use a "," before a coordinator
		arr = ["and", "but", "yet", "or", "nor", "for", "so"]
		if((X[i-1] in arr) and y_1==t2i("COMMA")):	return 1
		return 0
	
	return 0

# convention_ucsd: i = 1 denotes the first element in X, to acces it use X[0] not X[1]
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
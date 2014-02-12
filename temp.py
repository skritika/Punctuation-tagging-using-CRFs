global pos_tags, a_func
pos_tags = ["CC","CD","DT","EX","FW","IN","JJ","JJR","JJS","LS","MD","NN","NNP","NNPS","NNS","PDT","POS","PRP","PRP$","RB","RBR","RBS","RP","SYM","TO","UH","VB","VBD","VBG","VBN","VBP","VBZ","WDT","WP","WP$","WRB"]
a_func = []
for p in pos_tags:
	for q in pos_tags:
		a_func.append(lambda x, pos, i, f: f and  (pos[i]==p and pos[i+1]==q))
a_func.append(lambda x, pos, i, f: f and  x[i][0].isupper())
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='but')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='and')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='or')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='however')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='therefore')
a_func.append(lambda x, pos, i, f: f and  x[i].lower()=='therefore')
#1300: f and p[i]=='NNP',
a_func.append(lambda x, pos, i, f: i==n+1 and x[0].lower() in ['were','have','can','was', 'who', 'what', 'why', 'where', 'do', 'is', 'whose', 'when', 'how','are'])
a_func.append(lambda x, pos, i, f: f and i==0 and pos[0]=="RB")
a_func.append(lambda x, pos, i, f: f and x[i] in ["-","--"])
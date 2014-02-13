from main import *
f1 = open('comma','w')
f2 = open('question_mark','w')
f3 = open('exclamation_mark','w')
f4 = open('colon','w')
f5 = open('commai','w')
counti = 0
com = 0
for i in range(len(train_data)):
	print i
	if 'COMMA' in train_labels[i]:
		x = train_data[i]
		y = train_labels[i]
		if not ('then' in x  or 'I' in x[1:] or 'otherwise' in x or 'Otherwise' in x or 'example' in x or 'please' in x or 'Please' in x or 'although' in x or 'Therefore' in x or 'therefore' in x or x[0]=='Also' or x[0].endswith('ly') or 'however' in x or 'However' in x):
			f1.write(str(train_data[i]))
			f1.write('\n')
			#f1.write(str(train_POS[i]))
			#f1.write('\n')	
			f1.write(str(train_labels[i]))
			f1.write('\n')
			f1.write('\n')
	'''	if ('I' in x):
			j = x.index('I')
			if(j<>0):
				counti = counti+1;
				if y[j-1]=='COMMA':
					com = com+1	
			f5.write(str(train_data[i]))
			f5.write('\n')
			#f5.write(str(train_POS[i]))
			#f5.write('\n')	
			f5.write(str(train_labels[i]))
			f5.write('\n')
print "I_results"
print counti
print com
'''
'''	if 'QUESTION_MARK' in train_labels[i]:
		f2.write(str(train_data[i]))
		f2.write('\n')
		f2.write(str(train_labels[i]))
		f2.write('\n')
		f2.write('\n')
	if 'EXCLAMATION_MARK' in train_labels[i]:
		f3.write(str(train_data[i]))
		f3.write('\n')
		f3.write(str(train_labels[i]))
		f3.write('\n')
		f3.write('\n')
	if 'COLON' in train_labels[i]:
		f4.write(str(train_data[i]))
		f4.write('\n')
		f4.write(str(train_labels[i]))
		f4.write('\n')
		f4.write('\n')
'''

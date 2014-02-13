from main import *
f1 = open('comma','w')
f2 = open('question_mark','w')
f3 = open('exclamation_mark','w')
f4 = open('colon','w')
for i in range(len(train_data)):
	print i
	if 'COMMA' in train_labels[i]:
		f1.write(str(train_data[i]))
		f1.write('\n')
		f1.write(str(train_labels[i]))
		f1.write('\n')
		f1.write('\n')
	if 'QUESTION_MARK' in train_labels[i]:
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

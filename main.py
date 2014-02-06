'''
Possible labels
	COMMA
	PERIOD
	QUESTION_MARK
	EXCLAMATION_POINT
	COLON
	SPACE

Low-level feature functions
	1. The current word is 'and, but, yet, or, nor, for, so' and the previous tag is COMMA. 
	2. The current word is 'however, consequently, otherwise, moreover, nevertheless', the previous tag is COMMA and the current tag is COMMA.
	3. The previous tag is 'PERIOD/EXCLAMATION_POINT/QUESTION_MARK' and the current tag is STOP.
	4. The previous tag is START, the current word is 'well, now, yes, moreover, furthermore, specifically, however, likewise, therefore, consequently, meanwhile'(transitional phrase) and the current tag is COMMA. Basically transitional phrase at the beginning of a sentence.
	Using POS

'''		
from helper import *

def collins_train(data, pos, labels, num_epochs):
	iterations = 0
	W = np.zeros(J, dtype=float)
	while(iterations < num_epochs):
		for i in range(10):
			X = [data[i], pos[i]]
			Y = y2int(labels[i]) #start and stop tags also appended
			W = W + collins_grad(X,Y,W)
	return W

def test(data, pos, labels, W):
	num_test = len(data)
	true_tags = 0
	tot_tags = 0
	for i in range(num_test):
		print i
		X = [data[i], pos[i]]
		Y = y2int(labels[i])
		Y_pred = decode(X,W)
		tot_tags += len(X)
		true_tags += sum(Y_pred==Y)
	print "prediction accuracy : " , true_tags/tot_tags , "%"

train_data = load_data('trainingSentences')
train_labels = load_data('trainingLabels')
train_POS = load_data('trainingPOS')
test_data = load_data('testSentences')
test_labels = load_data('testLabels')
test_POS = load_data('testPOS')

collins_train(train_data, train_POS, train_labels, 3)
#test(test_data, test_POS, test_labels,np.ones(J, dtype=float))

#use this once before starting the training
#def cache_POS(data, file_name ):
#	f = open('punctuationDataset/'+file_name+".txt", "w")
#	for i in range(len(data)):
#		f.write(' '.join(POS(data[i])) + '\n')
#	f.close()
	
#cache_POS(test_data, 'testPOS')
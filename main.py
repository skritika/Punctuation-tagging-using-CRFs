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

def collins_train(data, labels, num_epochs):
	iterations = 0
	W = np.zeros(J, dtype=float)
	while(iterations < num_epochs):
		for i in range(10):
			X = data[i]
			Y = y2int(labels[i]) #start and stop tags also appended
			W = W + collins_grad(X,Y,W)
	return W

def test(data, labels, W):
	num_test = len(data)
	true_tags = 0
	tot_tags = 0
	for i in range(num_test):
		print i
		X = data[i]
		Y = y2int(labels[i])
		Y_pred = decode(X,W)
		tot_tags += len(X)
		true_tags += sum(Y_pred==Y)
	print "prediction accuracy : " , true_tags/tot_tags , "%"

train_data = load_data('punctuationDataset/trainingSentences.txt')
train_labels = load_data('punctuationDataset/trainingLabels.txt')
test_data = load_data('punctuationDataset/testSentences.txt')
test_labels = load_data('punctuationDataset/testLabels.txt')

collins_train(train_data, train_labels, 3)
#test(test_data, test_labels,np.ones(J, dtype=float))

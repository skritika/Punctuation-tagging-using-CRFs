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

def train(train_data, train_labels):
	'''Trains model using the training data
	for i in range(len(train_data)):
		l = train_labels[i].split(' ')
		print POS(train_data[i]) 
		print l
		'''
	num_epochs = 2
	iterations = 0
	lamda = 0.05
	W = np.zeros(J, dtype=float)
	while(iterations < num_epochs):
		for i in range(len(train_data)):
			X = train_data[0].split()
			Y = y2int(train_labels[0].split())
			W = W + lamda * collins_grad(X,Y,W)
			print i
	return W

def test(test_data, test_labels):
	'''Function to test the trained model on test data'''	
	#print test_data[0]
	#print test_labels[0]

train_data = load_data('punctuationDataset/trainingSentences.txt')
train_labels = load_data('punctuationDataset/trainingLabels.txt')
test_data = load_data('punctuationDataset/testSentences.txt')
test_labels = load_data('punctuationDataset/testLabels.txt')

train(train_data, train_labels)
#test(test_data, test_labels)

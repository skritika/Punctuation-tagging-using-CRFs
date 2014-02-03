from helper import *

def train(train_data, train_labels):
	'''Trains model using the training data'''	
	for i in range(len(train_data)):
		l = train_labels[i].split(' ')
		if(i==100):
			print POS(train_data[i]) 
			print l

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



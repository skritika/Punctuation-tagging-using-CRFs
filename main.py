from helper import *

def train(train_data, train_labels):
	'''trains model using the training data'''	
	print train_data[0]
	print train_labels[0]


def test(test_data, test_labels):
	'''test on testing data'''	
	print test_data[0]
	print test_labels[0]

train_data = load_data('punctuationDataset/trainingSentences.txt')
train_labels = load_data('punctuationDataset/trainingLabels.txt')
test_data = load_data('punctuationDataset/testSentences.txt')
test_labels = load_data('punctuationDataset/testLabels.txt')

train(train_data, train_labels)
test(test_data, test_labels)



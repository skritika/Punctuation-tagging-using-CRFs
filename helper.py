import nltk.tag

def load_data(file_path):
	f = open(file_path, 'r')
	list_data = f.readlines()
	return list_data	

def POS(sentence):
	tokens = nltk.word_tokenize(sentence)
	pos = nltk.pos_tag(tokens)
	tags = []
	for each in pos:
		tags.append(each[1])
	return tags

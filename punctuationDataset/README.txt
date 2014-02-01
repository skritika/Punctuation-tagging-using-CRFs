This dataset was generated from the Enron emails dataset at http://verbs.colorado.edu/enronsent/.

We filtered sentences that used complicated punctuation, like quotes and parentheses. We also
removed sentences that had more than two words not found in the unix dictionary. To make the
sentences more like text messages, we filtered out sentences without pronouns based on the chart
at http://en.wikipedia.org/wiki/English_personal_pronouns

The data files included are:
testLabels.txt
testSentences.txt
trainingLabels.txt
trainingSentences.txt

The *Sentences.txt files contain sentences without punctuation, one sentence on each line.
Each line in *Labels.txt gives the sequence of tags representing the punctuation marks that are
applied to the corresponding line in *Sentences.txt.

The possible tags are:
COMMA
PERIOD
QUESTION_MARK
EXCLAMATION_POINT
COLON
SPACE

Each word gets a single tag, representing the punctuation mark that follows that word. If the
word does not have a punctuation, the tag SPACE is used.

Example:

==> trainingLabels.txt <==
COMMA SPACE SPACE SPACE PERIOD
SPACE SPACE SPACE SPACE PERIOD
SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE QUESTION_MARK
SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE SPACE COMMA SPACE SPACE SPACE SPACE PERIOD
SPACE SPACE SPACE SPACE SPACE PERIOD
...

==> trainingSentences.txt <==
Therefore your feedback is critical
Thank you for your participation
Are the units he is selling significantly different from yours
As far as being an investor in a new project I am still very interested
Call or email with your thoughts
...

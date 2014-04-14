#!/usr/bin/python
import sys
import argparse
from collections import Counter

# list to store every n-gram in
ngrams = []
# save where the program is in the corpus
position = 0;

# parse command line arguments
parser = argparse.ArgumentParser(description="Get ngrams")
parser.add_argument('-corpus', metavar = 'textFile', type=str, help="flag for corpus")
parser.add_argument('-n', metavar='n', type=int, help="flag for ngram")
parser.add_argument('-m', metavar='m', type=int, help="flag for top m")
args = parser.parse_args()

# save command line arguments
nArg = vars(args)['n']
mArg = vars(args)['m']
textArg = vars(args)['corpus']

# initialize amount of words in n-gram
if(nArg != "None"):
	n = nArg
else:
	n = 3

# initialize how many of the most frequent sequences will be displayed
if(mArg != "None"):
	m = mArg
else:
	m = 3

# initialize which corpus is used
if(textArg != "None"):
	textFile = textArg
else:
	textFile = "train.txt"

# give user feedback on what variables are used
print "Corpus used: " + textFile + ", finding " + str(n) +  " words, displaying top " + str(m) + " sequences."

# read each line in the corpus and append into one long string
f = open(textFile, "r")
lines = f.readlines()
text = ""
for i in lines:
	text += i

# split the corpus and save as a list with all newlines, whitespace etc left out
wordArray = text.split()

# get all n-grams in the list by taking all words from the current position, 
# to the current position+n. Increment the position after each n-gram
for i in range(0, len(wordArray)-n+1):
	ngrams.append(" ".join(wordArray[position:position+n]))
	position+=1

# use the Counter class to create a dictionary where they key is the n-gram
# and the frequency is the value
countDict = Counter(ngrams)

# formatted print: output the m most frequent n-grams with their frequencies
# use count to print a ranking along with the output
count = 0
for k in countDict.most_common(m):
	count+=1
	print str(count) + ": '" + k[0] + "' is found " + str(k[1]) + " times."
print "Total frequencies: " + str(sum(countDict.values()))

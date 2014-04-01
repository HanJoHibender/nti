#!/usr/bin/python
import sys
import argparse
from collections import Counter

ngrams = []
position = 0;

parser = argparse.ArgumentParser(description="Get ngrams")
parser.add_argument('-corpus', metavar = 'textFile', type=str, help="flag for corpus")
parser.add_argument('-n', metavar='n', type=int, help="flag for ngram")
parser.add_argument('-m', metavar='m', type=int, help="flag for top m")
args = parser.parse_args()

nArg = vars(args)['n']
mArg = vars(args)['m']
textArg = vars(args)['corpus']

if(nArg != "None"):
	n = nArg
else:
	n = 3

if(mArg != "None"):
	m = mArg
else:
	m = 3

if(textArg != "None"):
	textFile = textArg
else:
	textFile = "train.txt"

print "Corpus used: " + textFile + ", finding " + str(n) +  " words, displaying top " + str(m) + " sequences."
f = open(textFile, "r")
lines = f.readlines()
text = ""
for i in lines:
	text += i

wordArray = text.split()
for i in range(0, len(wordArray)):
	ngrams.append(" ".join(wordArray[position:position+n]))
	position+=1
countDict = Counter(ngrams)
count = 0
for k in countDict.most_common(m):
	count+=1
	print str(count) + ": " + k[0] + "' is found " + str(k[1]) + " times."

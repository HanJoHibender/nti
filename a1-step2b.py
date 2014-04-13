#!/usr/bin/python
from __future__ import division
import sys
import argparse
from collections import Counter


def conProb(sequence):
	nGramCount = 0
	nMinOneGramCount = 0
	prob = 0.0 
	firstwords = sequence.rsplit(' ', 1)[0]
	for k in countDict.most_common():
		if k[0] == sequence:
			nGramCount = k[1]
	for l in countDict2.most_common():
		if l[0] == firstwords:
			nMinOneGramCount = l[1]	
	if nMinOneGramCount != 0:
		prob = float(nGramCount) / float(nMinOneGramCount)
	return prob


def makeString(textFile):
	fi = open(textFile, "r")
	lines = fi.readlines()
	text = start
	print "Corpus used: " + textFile + ", finding " + str(n) +  " words, displaying top " + str(m) + " sequences."
	prev = ""
	for i in lines:
		if(prev == "\n" and i == "\n"):
			continue
		if(i=="\n"):
			text+=stop
		text+=i
		if(i=="\n"):
			text+=start
		prev = i
	text += stop	
	return text	

# list to store every n-gram in
ngrams = []
ngrams2 = []
# save where the program is in the corpus
position = 0
position2 = 0
# frequencies
countDict = {}
countDict2 =  {}

start = "<s> "
stop = " </s>"
# parse command line arguments
parser = argparse.ArgumentParser(description="Get ngrams")
parser.add_argument('-corpus', metavar = 'textFile', type=str, help="flag for corpus")
parser.add_argument('-n', metavar='n', type=int, help="flag for ngram")
parser.add_argument('-m', metavar='m', type=int, help="flag for top m")
parser.add_argument('-conditional', metavar='probFile', type=str, help="flag for conditional probabilities file")
parser.add_argument('-sequence', metavar='seqFile', type=str, help="flag for sequences file")
args = parser.parse_args()

# save command line arguments
nArg = vars(args)['n']
mArg = vars(args)['m']
textArg = vars(args)['corpus']
probArg = vars(args)['conditional']
seqArg = vars(args)['sequence']

if(nArg is not None):
	n = nArg
else:
	n = 3

# initialize how many of the most frequent sequences will be displayed
if(mArg is not None):
	m = mArg
else:
	m = 3

# initialize which corpus is used
if(textArg is not None):
	textFile = textArg
else:
	textFile = "train.txt"

if(probArg is not None):
	probFile = probArg
else:
	probFile = "standard.txt"

if(seqArg is not None):
	seqFile = seqArg
else:
	seqFile = "sequence.txt"	

# read each line in the corpus and append into one long string
try:
	text = makeString(textFile)
	
except IOError:
	print "I cannot find or read the file '" + textFile + "'. Exiting."
	sys.exit(0)
# split the corpus and save as a list with all newlines, whitespace etc left out

#print text
wordArray = text.split()
wordArray2 = wordArray
n2 = n-1
#print wordArray
# get all n-grams in the list by taking all words from the current position, 
# to the current position+n. Increment the position after each n-gram
for i in range(0, len(wordArray)-n+1):
	gramAr = wordArray[position:position+n]
	#print gramAr
	if("<s>" in gramAr and "</s>" in gramAr):
		position+=1
		continue
	gram = " ".join(gramAr)
	ngrams.append(gram)
	position+=1
for j in range(0, len(wordArray2)-n+1):
	gram2Ar = wordArray2[position2:position2+n2]
	if("<s>" in gram2Ar and "</s>" in gram2Ar):
		#print gram2Ar
		position2+=1
		continue
	gram2 = " ".join(gram2Ar)
	ngrams2.append(gram2)
	position2+=1
# use the Counter class to create a dictionary where they key is the n-gram
# and the frequency is the value
#print ngrams
countDict  = Counter(ngrams)
countDict2 = Counter(ngrams2)

# formatted print: output the m most frequent n-grams with their frequencies
# use count to print a ranking along with the output
count = 0
count2 = 0

for k in countDict.most_common(m):
	count+=1
	print str(count) + ": '" + k[0] + "' is found " + str(k[1]) + " times."
print "Total frequencies: " + str(sum(countDict.values()))
for l in countDict2.most_common(m):
	count2+=1
	print str(count2) + ": '" + l[0] + "' is found " + str(l[1]) + " times."
print "Total frequencies: " + str(sum(countDict2.values()))

try: 
	seq = open(seqFile, "r")
	seqs = seq.readlines()
	for r in seqs:
		r = r.rstrip('\n')
		print r
		print "Prob of '" + r + "' is " + str(conProb(r))
except IOError:
	print "I cannot find or read the file '" + seqFile + "'. Exiting."

# use probFile
try:
	g = open(probFile, "r")
	sequences = g.readlines()

	for h in sequences:
		if(len(h.split()) == n):
			h = h.rstrip('\n') 
			print "Probability of '" + h + "' is " + str(conProb(h))
		else:
			continue
except IOError:
	print "I cannot find or read the file '" + probFile + "'. Exiting."
	sys.exit(0)


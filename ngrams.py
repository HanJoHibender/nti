from collections import Counter
n=2
m=4
ngrams = []
position = 0;
currentGram = ""
f = open("train.txt", "r")
lines = f.readlines()
text = ""
print lines
for i in lines:
	text += i
print text

wordArray = text.split()
print wordArray
for i in range(0, len(wordArray)):
	ngrams.append(" ".join(wordArray[position:position+n]))
	
	position+=1
#with open("train.txt") as f:
#	while True:
#		f.seek(position)
#		c = f.read(n)
#		if not c:
#			print "End of file"
#			break
#		position+=1
#		ngrams.append(c)
print ngrams
countDict = Counter(ngrams)
#print countDict['Of']
#print countDict['of']
#print countDict['OF']
print countDict.most_common(m)

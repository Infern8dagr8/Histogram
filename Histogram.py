import re
from operator import itemgetter

with open('input.txt', 'r') as f:
	histo = {}
	maxlen = 0 # for padding later
	
	for line in f:
		line = line.lower()
		line = re.sub('\.|,|!|\?|\n|\(|\)|"|&', '', line) # Pretty sure that's all common punctuation, excluding ' and -
		words = line.split()
		
		
		for word in words:
			if word not in histo:
				histo[word] = 0
			
			if len(word) > maxlen:
				maxlen = len(word)
			
			histo[word] += 1
	
	sortedWords = sorted(histo.items(), key=lambda item: item[1], reverse=True)
	
	out = ""
	for word, val in sortedWords:
		out += word.rjust(maxlen) + " | "
		for i in range(val):
			out += "="
		
		out += " (" + str(val) + ")\n"
	with open("output.txt", "w") as o:
		o.write(out)
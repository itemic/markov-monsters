# Starting using this tutorial: https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6

import random

def make_pairs(letter):
	for i in range(len(letter)-1):
		yield (letter[i], letter[i+1])

def create_corpus(filename):
	# this file should be a newline-delineated file
	file = open(filename, encoding="utf8").read()
	corpus = file.lower().split()
	dictionary = {}
	for word in corpus:
		pair = make_pairs(word)
		for l1, l2 in pair:
			if l1 in dictionary.keys():
				dictionary[l1].append(l2)
			else:
				dictionary[l1] = [l2]
	return dictionary

def generate(dictionary, length=8):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	seed = random.sample(dictionary.keys(), 1)
	chain = seed
	for i in range(length):
		# check for non-alpha characters
		try:
			chain += random.choice(dictionary[chain[-1]])
		except KeyError:
			chain += random.choice(alphabet)
		
	
	name = "".join(chain).title()
	return name

frequencies = create_corpus("pokemon.txt")

for x in range(10):
	print(generate(frequencies, 9))



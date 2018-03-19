import random

pokemon_list = open('pokemon.txt', encoding="utf8").read()
# print(pokemon_list)

corpus = pokemon_list.lower().split()
# print(corpus)

def make_pairs(letter):
	for i in range(len(letter)-1):
		yield (letter[i], letter[i+1])

# pairs = make_pairs('bepis')

word_dict = {}

for pokemon in corpus:
	pair = make_pairs(pokemon)
	for letter1, letter2 in pair:
		if letter1 in word_dict.keys():
			word_dict[letter1].append(letter2)
		else:
			word_dict[letter1] = [letter2]

# print(word_dict)

first_char = random.sample(word_dict.keys(), 1)

chain = [first_char]
string_chain = first_char
size = 8
print(string_chain)
for i in range(size):
	
	last_letter = string_chain[-1]
	string_chain += random.choice(word_dict[last_letter])
	# chain.append(random.choice(word_dict[last_letter[0]]))
	
string_chain[0] = string_chain[0].upper()
print("".join(string_chain))
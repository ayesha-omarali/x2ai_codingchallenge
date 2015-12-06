from __future__ import print_function
from nltk.util import ngrams

# input: String_1, String_2
# output: array of words only in String_2

def mapping(s1, s2):
	"""
	Outputs array of words only in String_2 from inputs String_1 and String_2

	>>> s1 = "The Dark Knight Rises"
	>>> s2 = "The Old Grandma Rises"
	>>> mapping(s1, s2)
	"The Rises"
	>>> s1 = "I only want candy"
	>>> s2 = "She loves candy corn and I want pumpkin pie"
	"candy I want"
	"""
	set1, s2 = set(s1.split(' ')), set(s2.split(' '))
	return set2.difference(s1)

# return all 5-grams of sentence 'show me an array of all the five-grams!'

def n_grams(sentence, n):
	""" 
	return all 5-gram of sentence, n = 5 input but can be any n.

	>>> sentence = 'show me an array of all the five-grams!'
	>>> n_grams(sentence, 5)
	('show', 'me', 'an', 'array', 'of')
	('me', 'an', 'array', 'of', 'all')
	('an', 'array', 'of', 'all', 'the')
	('array', 'of', 'all', 'the', 'five-grams')
	
	"""

	[print(x) for x in ngrams(sentence.split(), n)]



# Modify allPermutations to return all permutations of user_input, 
# using the lookup function


def lookup(placeholder):
    if placeholder == '<<NAME>>':
        return ['ayesha','eugene!','MIChiel','TESS','einstein1','eisenhower']
    if placeholder == '<<FEELING>>':
        return ['AWESOME!','Amazing','Brilliant...','great']
    return ['blah','blah','blah']
                
def allPermutations(user_input):

	"""
	>>> print(allPermutations('<<NAME>> <<FEELING>>')) 
	ayesha AWESOME!
	ayesha Amazing
	ayesha Brilliant...
	ayesha great
	eugene! AWESOME!
	eugene! Amazing
	eugene! Brilliant...
	eugene! great
	...
	"""

	name = lookup('<<NAME>>')
	feeling = lookup('<<FEELING>>')
	permutations = []
 
	for i in name:
		for j in feeling:
			temp = user_input.replace('<<NAME>>', i)
			permutations.append(temp.replace('<<FEELING>>', j))
	return permutations

print(allPermutations('Hi, I\'m <<NAME>>, and I feel <<FEELING>>!'))


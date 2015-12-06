from nltk.util import ngrams

# input: String_1, String_2
# output: array of words only in String_2

def mapping(s1, s2):
	set1, s2 = set(s1.split(' ')), set(s2.split(' '))
	return set2.difference(s1)

# return all 5-grams of sentence 'show me an array of all the five-grams!'

def n_grams(sentence, n):
	return ngrams(sentence.split(), 5)


# Modify allPermutations to return all permutations of user_input, 
# using the lookup function


def lookup(placeholder):
    if placeholder == '<<NAME>>':
        return ['ayesha','eugene!','MIChiel','TESS','einstein1','eisenhower']
    if placeholder == '<<FEELING>>':
        return ['AWESOME!','Amazing','Brilliant...','great']
    return ['blah','blah','blah']
                
def allPermutations(user_input):
	name = lookup('<<NAME>>')
	feeling = lookup('<<FEELING>>')
	
	permutations = []
	# r i in name:
		for j in feeling:
			permutations += string.replace(user_input, '<<NAME>>', name[i]).replace(user_input, '<<FEELING>>', name[j])
	
	return permutations

print(allPermutations('Hi, I\'m <<NAME>>, and I feel <<FEELING>>!'))
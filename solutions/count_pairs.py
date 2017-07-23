
import random

def generate_string(N, alphabet='ACGT'):
    return ''.join([random.choice(alphabet) for i in range(N)])





dna = generate_string(10)
pair = 'CG'


# Returns the number of occurences of a 
# pair of characters in a  DNA string
def count_pairs(dna,pair):
	return dna.count(pair);



print ('{} appears in {} dna: {} times'.format(pair, dna, count_pairs(dna, pair)))
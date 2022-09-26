import streamlit as st 
import names
from ultimate_wordlist import animals_list,adjectives_list,adverbs_list,positive_wordlist,negative_wordlist
import random 
import string

# Fxn
def generate_random(mylist:list,number_of_words:int=7)->list:
	results = [random.choice(mylist) for i in range(number_of_words)]
	return results

def custom_filter(mylist,start_char):
	results = [i for i in mylist if i.startswith(start_char)]
	# results = list(filter(lambda x: x.startswith(start_char),mylist))# method 2
	return results


def randomize(category,number_of_words):
	return {
	'First Names':lambda: [names.get_first_name() for i in range(number_of_words)],
	'Last Names':lambda: [names.get_last_name() for i in range(number_of_words)],
	'Positive Words':lambda: generate_random(positive_wordlist,number_of_words),
	'Negative Words':lambda: generate_random(negative_wordlist,number_of_words),
	'Adverb':lambda: generate_random(adverbs_list,number_of_words),
	'Adjectives':lambda: generate_random(adjective_list,number_of_words),
	'PetNames':lambda: generate_random(animals_list,number_of_words),
	}.get(category,lambda:'None Found')()
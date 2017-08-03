from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

text = "you are what you eat"

def count_words(text):
	"""count the number of times a word ocurrs in a text. Return a dictionary"""
	text = text.lower()
	skips = [".",",",";","'",'"']
	for ch in skips:
		text = text.replace(ch, "")
	word_counts = {}
	for word in text.split(" "):
		#know word
		if word in word_counts:
			word_counts[word] += 1
		else:
			word_counts[word] = 1
		
	return word_counts
	
#print (count_words(text))

def count_words_distribution(text):
	word_counts = count_words(text)
	values = list(word_counts.values())
	values = sorted(values)
	print (values)
	count_distribution = {x: values.count(x) for x in values}
	print (count_distribution)
	
count_words_distribution(text)
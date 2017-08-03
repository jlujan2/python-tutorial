from collections import Counter
import os
import pandas as pd
import matplotlib.pyplot as plt

text = "This comprehension check is to check for comprehension."

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
	
print (count_words(text))

def count_words_fast(text):
	"""count the number of times a word ocurrs in a text. Return a dictionary"""
	text = text.lower()
	skips = [".",",",";","'",'"']
	for ch in skips:
		text = text.replace(ch, "")
		
	word_counts = Counter(text.split(" "))
	
	return word_counts
	
print (len(count_words_fast(text)))
	
def read_book(title_path):
	"""read a book and return it as a string"""
	with open(title_path, "r", encoding="utf8") as current_file:
		text = current_file.read()
		text.replace("\n","").replace("\r","")
	return text
	
def word_stats(word_counts):
	"""return number of unique words and word frequencies"""
	num_unique = len(word_counts)
	counts = word_counts.values()
	return (num_unique, counts)
	
text = read_book("Romeo and Juliet.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print (num_unique, counts)



book_dir = "./books"
stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))
title_num = 1
for language in os.listdir(book_dir):
	for author in os.listdir(book_dir + "/" + language):
		for title in os.listdir(book_dir + "/" + language + "/" + author):
			inputfile = book_dir + "/" + language + "/" + author + "/" +title
			print(inputfile)
			text = read_book(inputfile)
			word_stats(count_words(text))
			(num_unique, counts) = word_stats(count_words(text))
			stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique
			title_num += 1

print (stats)
print (stats.tail())
table = pd.DataFrame(columns = ("name", "age"))
table.loc[1] = "James", 32
table.loc[2] = "Jss", 22




plt.plot(stats.length, stats.unique, "bo")
plt.show()
plt.loglog(stats.length, stats.unique, "bo")
plt.show()

plt.figure(figsize=(10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "green")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")
plt.show()
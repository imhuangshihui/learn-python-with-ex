'''
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
'''

import string
with open("words.txt", "r") as file:
    word_dict={}
    for line in file:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.lower().strip().strip(string.punctuation)
            if word not in word_dict:
                word_dict[word]
    print(word_dict)

# Write a Python program to split a list based on first character of word.
import itertools
from itertools import groupby
from operator import itemgetter
sentence = input("Enter the sentence")
input = list(sentence.split())
def split_by_first_char(input):
    for letter,words in groupby(sorted(input), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(word)
        
    

print(split_by_first_char(input))
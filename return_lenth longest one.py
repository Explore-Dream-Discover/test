# -*- coding: utf-8 -*-
"""
Created on Sat May 21 00:46:27 2022

@author: pavan
"""

upper_limit = int(input("Enter the upper range"))
lower_linit = int(input("enter lower range")) 
words = list()

for i in range(lower_linit,upper_limit):
    words.append(input("Enter the string"))
  
    
def longest_word(word):
    word_sort = sorted(word,key=(5
                                 len))
    result =   word_sort[-1]
    
    return result,len(result)

print(longest_word(words))  
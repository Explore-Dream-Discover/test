# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:43:23 2022

@author: pavan
"""

#remove the characters which have odd index values of a given string.

word = input("enter word")
def odd_values_string(word):
    result =list()
    for index in range(len(word)):
        if index % 2 == 0:
            result.append(word[index])
            return result
        
        
print(odd_values_string(word
                        ))        
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:27:20 2022

@author: pavan
"""
import string

word = input("enter the word")

def extract_first_last_letters(word):
    """
    

    Parameters
    ----------
    word : STRING
        string to extract first and latest letter 

    Returns
    -------
    result:first and last 2 words in a word

    """
    
    #convert word to list
    if len(word)<2:
        return ''
    return word[0:2],word[-2:]

print(extract_first_last_letters(word))
    
    
   
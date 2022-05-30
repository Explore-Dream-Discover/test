# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:48:54 2022

@author: pavan
"""


word =input("Enter the word")

def second_occurence_of_word(word):
    """
    


    Parameters
    ----------
    word : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    first_char = word[0]
    second = word.replace(first_char,"$")
    result = first_char + second[1:]
    return result

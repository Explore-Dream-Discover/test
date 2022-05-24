# -*- coding: utf-8 -*-
"""
Created on Sat May 21 22:24:39 2022

@author: pavan
"""

import string

word = "tender"

def first3_words(word):
    s1 = list(word)
    result = s1[0:3]
    return result 

print(first3_words(word))
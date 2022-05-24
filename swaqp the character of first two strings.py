# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:58:37 2022

@author: pavan
"""
s1 = "pavan","Ducati"


def swap_first_letter_of_two_strings(s1):
    first_letter_first_word = s1[0][0]
    first_letter_second_word = s1[1][0]
    
    first_word_result = first_letter_second_word + s1[0][1:]
    second_word_result = first_letter_first_word + s1[1][1:]
    
    return first_word_result,second_word_result

print(swap_first_letter_of_two_strings((s1)))
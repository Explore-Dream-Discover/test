# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:30:11 2022

@author: pavan
"""

word = "rajastan"  
 
def swap_first_last_letter(word):
    
    w1 = list(word)
    print("before swapping")
    print(w1)
    
    first =w1[0]
    last = w1[-1]
    temp = 0
    
    print("before sqping")
    print("first",first)
    print("last",last)
    
    temp = first
    first = last
    last =temp
    
    print("After sqping")
    print("first",first)
    print("last",last)
    
    w1[0] = first
    w1[-1] = last
    
    
    
    return w1


print(swap_first_last_letter(word))
     
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 00:10:54 2022

@author: pavan
"""
s1 = input()


def add_ing(s1) :
    if len(s1) > 3 :
        if s1[-3:] != "ing":
            s1 +="ing"
            
        else:
            s1 +="ly"
    return s1        


print(add_ing(s1))
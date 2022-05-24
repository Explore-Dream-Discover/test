# -*- coding: utf-8 -*-
"""
Created on Sat May 21 00:30:25 2022

@author: pavan
"""
s1 = input("Enter the string")


def replace_string(s1):
    snot = s1.find("not")
    spoor = s1.find("poor")
    
    if spoor > snot and snot > 0 and spoor > 0:
        s1 =s1.replace(s1[snot:(spoor)+4],"good")
        return s1
    else:
        return s1
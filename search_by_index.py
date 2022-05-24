# -*- coding: utf-8 -*-
"""
Created on Sat May 21 12:16:23 2022

@author: pavan
"""

word = input('Enter the word')
index_no = int(input("Enter the Index number"))


def search_by_index(word,index_no):
    list1 = list(word)
    return list1[index_no]


print(search_by_index(word,index_no))
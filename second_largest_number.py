# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:55:34 2022

@author: pavan
"""

number = int(input("Enter the number"))
scores =list()

def second_largest_number(number):
    for no in range(number):
        exam_scores = int(input("Enter the exam_score"))
        scores.append(exam_scores)
    s1 = set(scores)
    s2 = list(s1)
    return s2[-2]


print(second_largest_number(number))    
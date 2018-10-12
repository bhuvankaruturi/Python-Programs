# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:33:07 2018

@author: bkarutur
"""

cadets = int(input())
scores = []
grades = []
for i in range(0, cadets):
    scores.append(int(input()))
    counter = 0
    for j in range(0, i):
        if scores[j] >= scores[i]:
            counter = counter + 1
    grades.append(cadets - counter)

print(grades)
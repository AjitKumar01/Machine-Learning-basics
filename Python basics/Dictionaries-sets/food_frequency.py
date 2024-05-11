#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:03:02 2022

@author: ajit
"""

foodItems = ['Paneer Butter Masala', 'Masala Dosa', 'Tomato Rice', 'Masala Dosa', 'Rice', 'Dal', 'Idli','Chicken 65',
             'Dal', 'Vada', 'Paneer Butter Masala', 'Dal', 'Masala Dosa']

freqDict = {}
maxN = 0

for food in foodItems:
    if food not in freqDict:
        freqDict[food] = 1
    else:    
        freqDict[food]+=1
    if freqDict[food]>maxN:
        maxN = freqDict[food]

answer = '~~~~~~~~~~~~~~~~'*250
for food in freqDict.keys():
    if(maxN == freqDict[food] and answer>food):
        answer = food
        
print(freqDict)

print('\nFood with the most occurences:', answer)

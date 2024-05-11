#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:39:57 2022

@author: ajit
"""

# Problem 5

size = 5

dictA = {}
dictB = {}

import random
for i in range(size):
    dictA[chr(65+i)] = random.randint(1,100)

for i in range(size):    
    dictB[chr(67+i)] = random.randint(1,100)

# a) Create a new dictionary by merging the above two without set.
print(dictA)
print(dictB)

dictC = {}

dictC.update(dictA)

print(dictC)

for key in dictB:
    if key in dictA.keys():
        dictC[key] = dictA[key] + dictB[key]
    else:
        dictC[key] = dictB[key]

print(dictC)

# b) Merge the above two by using set

dictC = {}

A = set(dictA.keys())
B = set(dictB.keys())

for alp in A-B:
    dictC[alp] = dictA[alp]

for alp in B-A:
    dictC[alp] = dictB[alp]

for alp in B&A:
    dictC[alp] = dictA[alp]+dictB[alp]

print(dictC)




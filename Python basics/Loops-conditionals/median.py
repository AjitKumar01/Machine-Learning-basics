#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:47:31 2022

@author: ajit
"""

import random

size = int(input('Enter size:'))
lst = random.sample(range(1,100), size)

print(lst)

lst.sort()

print(lst)

if size%2 == 0:
    median = (lst[size//2] + lst[size//2-1])/2
else:
    median = lst[size//2]
    
print('Median of the list:', median)

sublist1 = lst[:size//2]
sublist2 = lst[size//2:]

print(sublist1)
print(sublist2)

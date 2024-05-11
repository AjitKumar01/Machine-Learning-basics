#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:37:52 2022

@author: ajit
"""

# Pascal's triangle

n = int(input('Enter a natural number:'))

if(n>=1):
    first = [1]
    print(first)
    
for i in range(n-1):
    second = []
    second.append(1)
    for j in range(0, len(first)-1):
        second.append(first[j]+first[j+1])
    second.append(1)
    print(second)
    first = second
        
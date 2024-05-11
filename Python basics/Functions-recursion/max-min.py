#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:50:29 2022

@author: ajit
"""

# Recurive function to find the maximum
def maxim(lst):
    if len(lst) == 1:
        return lst[0]
    
    return max(lst[0], maxim(lst[1:]))


# Recursive function to find the minimum
def minim(lst):
    if len(lst) == 1:
        return lst[0]
    
    return min(lst[0], minim(lst[1:]))

lst = [7,4,3,1,2,1,100,-34]
lst1 = [3,3,3,3]

print(maxim(lst))
print(minim(lst))
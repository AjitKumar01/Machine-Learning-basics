#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 15:50:26 2022

@author: ajit
"""

def count(N,M):
    if(N>100 or N<0):
        return 0
    if(M>9 or M<0):
        return 0
    
    if(N<M):
        return 0
    
    countM = 0
    for str1 in str(N):
        if str1 == str(M):
            countM+=1
    
    return countM + count(N-1,M)


N = int(input('Enter an integer:'))
M = int(input('Enter another one:'))

print(count(N,M))

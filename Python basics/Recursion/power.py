#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:08:35 2022

@author: ajit
"""

# The power of a variable: x**n

def power(x,n):
    if n == 0:
        return 1
    if x == 0:
        if x == 0 and n<0:
            print('Division by zero is undefined')
        return 0
    
    k = abs(n)
    answer = 1.0
    for i in range(k):
        answer*=x
     
    if n<0: 
        return 1/answer
    
    return answer    
    
        
x = float(input('Enter a number:'))
n = int(input('Enter an integer:'))

print(power(x,n))
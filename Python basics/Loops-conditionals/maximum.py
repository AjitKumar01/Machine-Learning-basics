#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 14:27:41 2022

@author: ajit
"""

num1, num2, num3 = input('Enter three numbers: ').split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

#a
# First way
if num1<=num2<=num3:
    print(num3, 'is the largest.')
elif num1<=num3<=num2:
    print(num2, 'is the largest.')
else:
    print(num1, 'is the largest.')
    
# Second way
if num1<num2:
    if num3<num2:
        print(num2, 'is the largest')
    else:
        print(num3, 'is the largest')
else:        
    if num3<num1:
        print(num1, 'is the largest')
    else:
        print(num3, 'is the largest')
        
# Third way

if num1<=num2 and num2<=num3:
    print(num3, 'is the largest.')
elif num3<=num2 and num1<=num2:
    print(num2, 'is the largest')
else:
    print(num1, 'is the largest')    
  
#b
# first way
if num1<num2:
    max1 = num2 if num2>num3 else num3
else:        
    max1 = num1 if num1>num3 else num3
print(max1, 'is the largest.')
     
# second way
max1 = (num1 if num1>num2 else num2) if (num1 if num1>num2 else num2)>num3 else num3
print(max1, 'is the largest.')

    
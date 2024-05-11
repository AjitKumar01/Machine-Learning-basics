#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 14:15:36 2022

@author: ajit
"""

#import math
number = int(input('Enter a number: '))

i = 2

while(i <= number//2):
    if(number%i == 0):
        break
    i+=1

if(number!=1 and i > number//2):
    print(f'{number} is a prime number.')
else:
    print(f'{number} is not a prime number.')
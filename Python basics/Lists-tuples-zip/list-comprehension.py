#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:12:45 2022

@author: ajit
"""

import random 

size = int(input('Enter size:'))
lst = random.sample(range(10,100), size)
print('List:', lst)

# Print even numbers
print('Even numbers:')
[print(num) for num in lst if num%2==0]

# Print odd numbers
print('Odd numbers:')
[print(num) for num in lst if num%2!=0]

# Print numbers divisible by 3
print('Numbers divisible by 3:')
[print(num) for num in lst if num%3==0]




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:39:21 2022

@author: ajit
"""

x = input('Enter a number:')

count = 0

for i in x:
    if ord(i)>=48 and ord(i)<=57: 
        count+=(ord(i) - 48)
    else:
        count+=(ord(i))

print('Sum of the digits:', count)    
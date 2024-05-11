#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:44:10 2022

@author: ajit
"""

#############-------------
#3

import random as rnd

rnd.seed(0)
x = [0 for i in range(5)]

print('\nThe random values are:')
for i in range(5):
    x[i] = rnd.random()
    print('\t', x[i])
    
print('\nValue after performing the arithmetic operations:',x[0]+x[1]-x[2]/x[3]*x[4])
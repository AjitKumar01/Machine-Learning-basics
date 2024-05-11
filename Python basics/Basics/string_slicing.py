#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:45:49 2022

@author: ajit
"""

#5

string = 'Sairam'

# When it takes three parameters the last one is for step.
print('\nPrinted string with two steps:',string[slice(0,len(string), 1)])

# Reverse a string
print('Reversed string:', string[slice(-1,-len(string)-1,-1)])
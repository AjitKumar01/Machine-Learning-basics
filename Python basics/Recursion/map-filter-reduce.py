#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 15:24:30 2022

@author: ajit
"""

# Map function - it returns a map object after applying the given function to each item in the iterable.

# It squares all the elements in the list - [0,1,2,3,...,9]
lst = list(map(lambda x:x**2, [num for num in range(10)]))
print(lst)

# Filter function - filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

# It filters all the even numbers between 0 and 9
lst = list(filter(lambda x: True if x%2==0 else False, [num for num in range(10)]))
print(lst)

# Reduce function - it takes a function and an iterable. 
# it accumulates and uses the function for each element in the iterable.
# for example - [1,2,3]
# At first it uses the function for 1 and 2, gets 3. Then, for the next iteration it uses 3(accumulated value) and 3,
# so finally return 6.

import functools
print(functools.reduce(lambda x,y:x+y, [num for num in range(4)]))



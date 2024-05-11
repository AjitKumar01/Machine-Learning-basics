#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 14:51:03 2022

@author: ajit
"""

# Continue statement is executed to skip the iteration. When it is executed, then the control goes directly
# to the next iteration(in case of for loop) or condition(in case of while loop).

i = 0
while(i<5):
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1
    

# Here 3 is skipped.

# In case of 'pass' statement nothing is exectuted. It is generally put future code.

i = 0
while(i<5):
    if(i==3):
        pass
    print(i)
    i+=1


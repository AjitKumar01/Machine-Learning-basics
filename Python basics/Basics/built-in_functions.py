#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:41:59 2022

@author: ajit
"""

#### 1
#  Built in functions with and without math module
import math

x = -2.45

if(x<0):
    print('Absolute value of x:', -x)
else:
    print('Absolute value of x:', x)
    

print('Absolute value of the number using in-built function:', math.fabs(x))

x = 5

product = 1
for i in range(1,x+1):
   product = product*i 

print('\nFactorial of the number:', product)
print('Factorial of the number: using in-built function:', math.factorial(x))

x = 5
print('\nSquare root of the number using in-built function:', math.sqrt(x))

x = 5.23
print('Cos of the number using in built function', math.cos(x))

# rounding functions

x = 2.34

if x>=0:
    print('\nFloored value of x:', int(x))
else:
    print('\nFloored value of x:', int(x)-1)
print('Floored value of x using in-built function:', math.floor(x))

if(x>0):
    print('\nCeiled value of x:', int(x)+1)
else:
    print('\nCeiled value of x:', int(x))
    
print('Ceiled value of x using in-built function:', math.ceil(x))









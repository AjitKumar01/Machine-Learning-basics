#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 15:00:35 2022

@author: ajit
"""

import math
num = float(input('Enter a number: '))

# a)exp(x)

sum1 = 1

for i in range(1,100):
    sum1 += ((num**i)/math.factorial(i))

print('Value of exp(num):', sum1, '\n')

# b)sin(x)

sum1 = 0

# for i in range(0,100):
#     temp = ( ((-1)**(i)) * ( num**(2*i+1)) / math.factorial(2*i+1) )
#     sum+=temp

term = num
sum1 = num

for i in range(1,100):
    term = (-1) * (term*num*num)/((2*i+1)*(2*i))
    sum1+=term
    
#print(math.sin(num))
print('\nValue of sin(num):', sum1)

# c) cos(x)    
sum1 = 0

# for i in range(0,100):
#     temp = ( ((-1)**(i)) * ( num**(2*i+1)) / math.factorial(2*i+1) )
#     sum+=temp

term = 1
sum1 = 1

for i in range(1,100):
    term = (-1) * (term*num*num)/((2*i)*(2*i-1))
    sum1+=term
    
#print(math.cos(num))
print('\nValue of cos(num):', sum1)
  


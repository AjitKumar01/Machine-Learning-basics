#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:00:11 2022

@author: ajit
"""

tupName = ('Ajit', 'Auro', 'Sandy')
tupAge =(23,25,23)
tupSalary = (10000, 12000, 15000)

print(tupName, tupAge, tupSalary) 

# Without list comprehension
lst = []
for i in range(len(tupName)):
    lst.append((tupName[i], tupAge[i], tupSalary[i]))

print(lst)

# With list comprehension

lst = [(tupName[i], tupAge[i], tupSalary[i]) for i in range(len(tupName))]
print(lst)

# With zip function

ite = zip(tupName, tupAge, tupSalary)

lst = list(ite)
print(lst)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:05:53 2022

@author: ajit
"""

lst = ['Ajit', 'Ajay', 'Rahul', 'Anil', 'Debasish']

print(lst)

lst.sort()

print(lst)

queryName = input('Enter a name: ')

index = 0

for stri in lst:
    if queryName < stri:
        break
    index+=1
    
lst.insert(index, queryName)

print('\nList after insertion:', lst)

queryName = input('Enter the name to be deleted: ')
try:
    lst.remove(queryName)
except:
    print('Name is not present in the list')

print('\n', lst)

queryName = input('Enter the name to be appended at the beginning: ')
lst.insert(0,queryName)

print('\nList after insertion at the beginning: ', lst)

i = 0

while i< len(lst):
    j = i+1
    while j< len(lst):
        if(lst[j] == lst[i]):
            lst.remove(lst[j])
        j+=1
    i+=1


print('\nList with unique elements: ', lst)

lst.sort()

print('\nSorted list: ', lst)



        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:28:25 2022

@author: ajit
"""

# Function for the reverse of words or sentence.

def funcReverse(givenStr, typ_of):
    if(typ_of == 'sentence'):
        return givenStr[::-1]
    
    lstStr = givenStr.split()
    
    new_Str = []
    
    for str1 in lstStr:
        new_Str.append(str1[::-1])
    
    return ' '.join(new_Str)

str1 = "The sun is hot"

print(funcReverse(str1, 'sentence'))
print(funcReverse(str1, 'words'))


# With the help of recursion.

def funcRec(givenStr, typ_of):
    if(typ_of == 'sentence'):
        return givenStr[::-1]

    lstStr = givenStr.split()
    
    a = lstStr[0][::-1]
    
    if len(lstStr) == 1:
        return a
    
    newStr = ' '.join(lstStr[1:])
    
    return ' '.join([a, funcRec(newStr, 'words').split()])
    
print(funcReverse(str1, 'sentence'))
print(funcReverse(str1, 'words'))
    

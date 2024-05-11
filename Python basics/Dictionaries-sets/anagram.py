#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 16:08:02 2022

@author: ajit
"""

def anagram(listStrings):
    
    length = [len(str1) for str1 in listStrings]
    
    # First check for lenght of each string
    for num in length:
        if num != length[0]:
            return False
        
    # Then check for the Characters
    for index in range(1,len(listStrings)):
        for char in listStrings[index]:
            if char not in listStrings[0]:
                return False
    
    return True
    

lstA = ['earth', 'heart', 'tearh']
lstB = ['earth', 'hear', 'ear']

print(anagram(lstA))
print(anagram(lstB))
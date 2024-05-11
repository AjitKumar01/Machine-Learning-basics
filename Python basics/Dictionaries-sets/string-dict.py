#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:21:01 2022

@author: ajit
"""

# Problem3

givenString = input('Enter the string:')

# a) Count the number of appearance and print the result in the form of a dictionary

letterDict = {}
for let in givenString:
    if let.isalpha():
        if let not in letterDict:
            letterDict[let] = 1
        else:
            letterDict[let]+=1

print(letterDict)

# b) Print the first unique letter in the string

for let in letterDict.keys():
    if letterDict[let] == 1:
        print('The first unique character is:', let)
        break

# c) Remove the duplicates from the string and print the new string

uniqueStr = []

for char in givenString:
    if char not in uniqueStr:
        uniqueStr.append(char)

print('\nNew string with unique characters')
print(*uniqueStr)
#print(newString)

# d) Remove the duplicates from the string and print the new string using set operations.

uniqueStr = set()

for char in givenString:
    uniqueStr.add(char)

print('\nNew string with unique characters')

lst = []
for a in givenString:
    if a in uniqueStr and a not in lst:
        print(a)
        lst.append(a)
        

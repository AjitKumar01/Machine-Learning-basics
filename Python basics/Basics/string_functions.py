#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:46:31 2022

@author: ajit
"""

#################--------------------------
#6

string = "hello, I could not have my lunch today."

# capitalize() - converts the first character to upper case.
print('\n',string.capitalize())

# isalpha() - returns true if all the characters are in the alphabet
print('\n',string.isalpha())

# upper() - converts a string to uppercase
print('\n',string.upper())

# lower() - converts a string to lowercase
print('\n',string.lower())

# title() - converts the first character of each word to upper case
print('\n',string.title())

# split() - splits the string wrt the blank spaces
print('\n',string.split())

# partition() - searches for a specifed string, and splits the string into a tuple containing three elements
print('\n',string.partition('have'))

# find() - finds the first occrence of the specified value
print('\n',string.find('have'))

# replace() - replaces a specified phrase with another specified phrase
print('\n',string.replace('lunch', 'breakfast'))
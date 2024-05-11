#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:31:31 2022

@author: ajit
"""

# Problem 1
# Three chosen sports
sports = ['Cricket', 'Football', 'Basketball']

# For taking input of new players
flag = True

# To make sure that the keys are uniqe
names = []

# The dictionary 
sportLike = {}

while flag:
    name = input('Enter the name of the player:')
    
    if name not in names:
        names.append(name)
        sportLike[name] = []
        
        for game in sports:
            ans = input('Do you like '+game+' ?(y/n): ')
            if ans == 'y' or ans == 'Y':
                sportLike[name].append(game)
        
        ansCont = input('Do you want to enter details of another player?(y/Y):')
        flag = ansCont == 'y' or ansCont == 'Y'
    
    else:
        print('Player name already exist! Please re-enter')
        
print('Dictionary:', sportLike)
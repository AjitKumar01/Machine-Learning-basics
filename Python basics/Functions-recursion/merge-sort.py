#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 15:00:40 2022

@author: ajit
"""

# Recursive function to print the sum

def call_sum(lst):
    if(len(lst)==0):
        return 0
    if(len(lst) == 1):
        return lst[0]
    
    return lst[0] + call_sum(lst[1:])

lst = [3,4,5,6,7,9,3]
lst1 = []

print(call_sum(lst))
    
# recursive function to get the ascending order of numbers
def merge(lst1, lst2):
    p1 = 0
    p2 = 0
    
    lst3 = []
    
    while(p1<len(lst1) and p2<len(lst2)):
        if lst1[p1]<lst2[p2]:
            lst3.append(lst1[p1])
            p1+=1
        else:
            lst3.append(lst2[p2])
            p2+=1
    
    while p1<len(lst1):
        lst3.append(lst1[p1])
        p1+=1
    
    while p2<len(lst2):
        lst3.append(lst2[p2])
        p2+=1
    
    return lst3

                
def merge_sort(lst):
    if(len(lst) == 1):
        return [lst[0]]
    
    mid = int(len(lst)/2)
    
    a = merge_sort(lst[:mid])
    b = merge_sort(lst[mid:])
    
    return merge(a,b)

lst = [3,4,5,6,7,9,3,9]
print(merge_sort(lst))

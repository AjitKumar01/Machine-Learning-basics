#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:48:31 2022

@author: ajit
"""

n = int(input('Enter n:'))

# Factorial using loops

factorial = 1 
for num in range(1,n+1):
    factorial*=num
print(factorial)

# factorial using recursion:

def fact(n):
    if(n<=0):
        return 1
    
    return n*fact(n-1)

print(fact(n))

# Fibonacci using loops
# [1,1,2,3,5,8,12,...]

fibo_list = [0]*(n+1)

if n>0:
    fibo_list[1] = 1
    for i in range(2,n+1):
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]

if n>0:
    print(fibo_list[n])
else:
    print(0)

# Fibonacci using recursions
def fibo(n):
    if(n<=0):
        return 0
    if(n==1):
        return 1
    
    return fibo(n-1)+fibo(n-2)
    
print(fibo(n))
    
    
    
    
    
    

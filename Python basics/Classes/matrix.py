#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:17:57 2022

@author: ajit
"""

import random

class Matrix:
    
    def __init__(self, rows = 0, col = 0):
        self.row = rows
        self.col = col
        
        self.val = [random.sample(range(0,20),col) for i in range(rows)]
    
    def __add__(self,other):
        if self.row != other.row  or self.col != other.col:
            print('\nUnequal rows or columns!')
            return
        
        M3 = Matrix(self.row, self.col)
        
        # Addition of two matrices
        M3.val  = [[sum(it1) for it1 in zip(*it)] for it in zip(self.val, other.val)]
        
        return M3
    
    def __sub__(self,other):
        if self.row != other.row  or self.col != other.col:
            print('\nUnequal rows or columns!')
            return
        
        M3 = Matrix(self.row, self.col)
        M3.val  = [[it1[0] - it1[1] for it1 in zip(*it)] for it in zip(self.val, other.val)]
        
        return M3
    
    def __mul__(self,other):
        if self.col != other.row:
            print('\nIncompatible matrices!')
            return
        
        M3 = Matrix(self.row, self.col)
        
        for i in range(self.row):
            for j in range(other.col):
                M3.val[i][j] = sum([self.val[i][k]*other.val[k][j] for k in range(self.col)])
        
        return M3
    
    def eleMul(self,other):
        if self.row != other.row  or self.col != other.col:
            print('\nUnequal rows or columns!')
            return
        
        M3 = Matrix(self.row, self.col)
        
        for i in range(self.row):
            for j in range(self.col):
                M3.val[i][j] = self.val[i][j] * other.val[i][j]
        
        return M3
    
    def scalarMul(self, num):
        M3 = Matrix(self.row, self.col)
        
        
        for i in range(self.row):
            M3.val[i] = list(map(lambda x: num*x, self.val[i])) 
        
        return M3
    
    def __str__(self):
        
        st = ''
        
        for i in range(self.row):
            for j in range(self.col):
                st = st+str(self.val[i][j])+'\t'
            st+='\n'
        
        return st
    
M1 = Matrix(2,2)
M2 = Matrix(2,2)

print('Matrix A:')
print(M1)

print('Matrix B:')
print(M2)

# Addition:
M3 = M1+M2
print('Addition:')
print(M3)

# Subtraction:
print('Subtraction:')
print(M1-M2)

# Multiplication:
print('Multiplication:')
print(M1*M2)

# Elementwise MAtrix Multiplication:
print('Element wise marix multiplication:')
print(M1.eleMul(M2))

# Scalar Multiplication:
print('Scalar multiplication for matrix A:')
print(M1.scalarMul(4))



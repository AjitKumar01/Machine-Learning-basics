#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 18:57:00 2022

@author: ajit
"""
# For complex class
class Complex:
    def __init__(self, real = 0, imag = 0):
        self._real = real
        self._imag = imag
        
    
    def __add__(self, other):
        c3 = Complex()
        c3._real = other._real + self._real
        c3._imag = other._imag + self._imag
        
        return c3
    
    def __sub__(self, other):
        c3 = Complex()
        c3._real = -other._real + self._real
        c3._imag = -other._imag + self._imag
        
        return c3
    
    def __mul__(self, other):
        c3 = Complex()
        c3._real = self._real*other._real - self._imag*other._imag
        c3._imag = self._real*other._imag + self._imag*other._real
        
        return c3
    
    def __truediv__(self, other):
        if other._real**2 + other._imag**2 == 0:
            print('Division by zero.')
            return
        
        # denominator
        den = other._real**2 + other._imag**2
        c3 = Complex()
        c3._real = (self._real*other._real + self._imag*other._imag)/den
        c3._imag = (self._imag*other._real - self._real*other._imag)/den
        
        return c3
    
    # For integer division
    def __floordiv__(self, other):
        if other._real**2 + other._imag**2 == 0:
            print('Division by zero.')
            return
        
        # denominator
        den = other._real**2 + other._imag**2
        c3 = Complex()
        c3._real = (self._real*other._real + self._imag*other._imag)//den
        c3._imag = (self._imag*other._real - self._real*other._imag)//den

        return c3
    def __str__(self):
        if self._real == 0 and self._imag == 0:
            return '0'
        
        if self._imag<0:
            return f'{self._real}{self._imag}i'
        
        return f'{self._real}+{self._imag}i'

import math
class DerivedComplex(Complex):
    
    def __init__(self, real, imag):
        super().__init__(real, imag)
    
    def reciprocal(self):
        c1 = Complex(1,0)
        return c1/self
    
    def conjugate(self):
        c1 = Complex(self._real, -self._imag)
        return c1
    
    def absoluteValue(self):
        
        c =  self*self.conjugate()
        
        return math.sqrt(c._real + c._imag)
        
    
        
D1 = DerivedComplex(2,3)
print(D1.reciprocal())
print(D1.conjugate())
print(D1.absoluteValue())

# Matrix multiplicaton
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
        
        for i in range(self.row):
            for j in range(self.col):
                M3.val[i][j] = self.val[i][j] + other.val[i][j]
        
        
        return M3
    
    def __sub__(self,other):
        if self.row != other.row  or self.col != other.col:
            print('\nUnequal rows or columns!')
            return
        
        M3 = Matrix(self.row, self.col)
        
        for i in range(self.row):
            for j in range(self.col):
                M3.val[i][j] = self.val[i][j] - other.val[i][j]
        
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
    
    def __str__(self):
        
        st = ''
        
        for i in range(self.row):
            for j in range(self.col):
                st = st+str(self.val[i][j])+'\t\t'
            st+='\n'
        
        return st
    

class MatrixDerived(Matrix):
    
    def __init__(self, row, col):
        super().__init__(row, col)
    
    def scalarMul(self, num):
        M3 = Matrix(self.row, self.col)
        M3.val = [[num]*self.col]*self.row
        
        return M3.eleMul(self)
    
    def powerMul(self, expo = 1):
        if(self.row != self.col):
            print('Unequal rows and columns')
            return
        
        M3 = Matrix(self.row, self.col)
        
        for i in range(M3.row):
            for j in range(M3.row):
                if i == j:
                    M3.val[i][i] = 1
                else:
                    M3.val[i][j] = 0
        
        for i in range(expo):
            M3*=self
        
        return M3
         
    
        
M1 = MatrixDerived(2,2)
print(M1)
print(M1.scalarMul(3))
print(M1.powerMul(3))

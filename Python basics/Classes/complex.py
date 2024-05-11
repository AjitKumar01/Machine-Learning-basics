#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:37:01 2022

@author: ajit
"""

class Complex:
    def __init__(self, real = 0, imag = 0):
        self._real = real
        self._imag = imag
    
    def addComplex(self, other):
        c3 = Complex()
        c3._real = other._real + self._real
        c3._imag = other._imag + self._imag
        
        return c3
    
    def subComplex(self, other):
        c3 = Complex()
        c3._real = -other._real + self._real
        c3._imag = -other._imag + self._imag
        
        return c3
    
    def mulComplex(self, other):
        c3 = Complex()
        c3._real = self._real*other._real - self._imag*other._imag
        c3._imag = self._real*other._imag + self._imag*other._real
        
        return c3
    
    def divComplex(self, other):
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
    def floorDivComplex(self, other):
        if other._real**2 + other._imag**2 == 0:
            print('Division by zero.')
            return
        
        # denominator
        den = other._real**2 + other._imag**2
        c3 = Complex()
        c3._real = (self._real*other._real + self._imag*other._imag)//den
        c3._imag = (self._imag*other._real - self._real*other._imag)//den

        return c3
    
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
        

# First complex number
c1 = Complex(1,2)

# Second complex number
c2 = Complex(2,3)

print('\nWithout operator overloading:\n')
c3 = c1.addComplex(c2)
print('Addition:',c3)

c3 = c1.subComplex(c2)
print('Subtraction:',c3)
 
c3 = c1.mulComplex(c2)
print('Multiplication:',c3)

c3 = c1.divComplex(c2)
print('Division:',c3)

c3 = c1.floorDivComplex(c2)
print('Floor division:',c3)

print('------------------------------------------------------')
print('\nWith operator overloading:\n')
c3 = c1+c2
print('Addition:',c3)

c3 = c1-c2
print('Subtraction:',c3)
 
c3 = c1*c2
print('Multiplication:',c3)

c3 = c1/c2
print('Division:',c3)

c3 = c1//c2
print('Floor division:',c3)


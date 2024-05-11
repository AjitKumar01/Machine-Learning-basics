#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:09:38 2022

@author: ajit
"""

class Polygon:
    def __init__(self, leng):
        self.length = leng
    
    def __str__(self):
        return str(self.length)
    
class Square(Polygon):
    def __init__(self, leng):
        super().__init__(leng)
    
    def findArea(self):
        return self.length**2;
    
S1 = Square(4)
print(S1.findArea())
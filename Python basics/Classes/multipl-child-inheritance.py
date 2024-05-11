#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:17:29 2022

@author: ajit
"""

class Department:
    def __init__(self, dn = ""):
        self.dname = dn
    
    def __str__(self):
        return self.dname
    
class Faculty:
    def __init__(self, fn = "", dn = ""):
        self.fname = fn
        self.dname = Department(dn)
        
    def __str__(self):
        return f'Faculty name: {self.fname}\nDepartment name: {self.dname}'

class Student:
    def __init__(self, sn = "", dn = ""):
        self.name = sn
        self.dname = Department(dn)
    
    def __str__(self):
        return f'Student name: {self.name}\nDepartment name: {self.dname}'

f1 = Faculty('Ramananthan','Engineering design')
print(f1)

s1 = Student('Ajay','Electrical Engineering')
print('\n',s1)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:47:46 2022

@author: ajit
"""

class Father:
    def __init__(self, fn = '', fa = 30, ft = set()):
        self.father_name = fn
        self.father_age = fa
        self.father_talent = ft
    
    def getFatherDetails(self):
        self.father_name = input('Enter father\'s name:')
        self.father_age = int(input('Enter father\'s age:'))
        self.father_talent = set(input('Enter father\'s talent:').split())

class Mother:
    def __init__(self, mn = '', ma = 30, mt = set()):
        self.mother_name = mn
        self.mother_age = ma
        self.mother_talent = mt
    
    def getMotherDetails(self):
        self.mother_name = input('Enter mother\'s name:')
        self.mother_age = int(input('Enter mother\'s age:'))
        self.mother_talent = set(input('Enter mother\'s talent:').split())

class Child(Mother, Father):
    def __init__(self):
        #Father.__init__(self, f.father_name, f.father_age, f.father_talent)
        #Mother.__init__(self, m.mother_name, m.mother_age, m.mother_talent)
        self.child_name = ''
        self.child_age = 10
        self.child_gender = 'M'
    
    def getChildDetails(self):
        Father.getFatherDetails(self)
        Mother.getMotherDetails(self)
        self.child_name = input('Enter Child\'s name:')
        self.child_age = int(input('Enter Child\'s age:'))
        self.child_gender = input('Enter Child\'s gender:')
        
    def printChildDetails(self):
        print('\nChild name:', self.child_name)
        print('Child age:', self.child_age)
        print('Child gender:', self.child_gender)
    
    def displayTalents(self):
        print('\nSimilar talents:',self.mother_talent & self.father_talent)
        
#father = Father('Ram', 50, {'singer', 'dancer', 'artist'})
#mother = Mother('Sunitha', 45, {'badminton', 'tennis', 'artist'})

child1 = Child()
child1.getChildDetails()
child1.printChildDetails()
child1.displayTalents()

        
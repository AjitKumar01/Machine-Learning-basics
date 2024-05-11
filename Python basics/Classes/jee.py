#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:24:54 2022

@author: ajit
"""

class Student:
    def __init__(self, sn = '', rn = 0):
        self.student_name = sn
        self.roll_number = rn
    
    def getDetails(self):
        self.student_name = input('Enter student name:')
        self.roll_number = input('Enter roll number:')
    
    def printDetails(self):
        print('\nStudent name: ', self.student_name)
        print('\nStudent roll number: ', self.roll_number)

class JEE(Student):
    def __init__(self, pm = 0, cm = 0, mm = 0):
        self.physics_marks = pm
        self.chem_marks = cm
        self.maths_marks = mm
    
    def getMarks(self):
        super().getDetails()
        self.physics_marks = int(input('Enter physics marks:'))
        self.chem_marks = int(input('Enter chemistry marks:'))
        self.maths_marks = int(input('Enter mathematics marks:'))
    
    def printDetails(self):
        super().printDetails()
        print('\nPhysics marks: ', self.physics_marks)
        print('\nChemistry marks: ', self.chem_marks)
        print('\nMaths marks: ', self.maths_marks)
        
class Semester(JEE):
    def __init__(self, courses = [], cgpa = 0.0):
        self.courses = courses
        self.cgpa = cgpa
        
    def getSemDetails(self):
        super().getMarks()
        self.courses = input('Enter the courses taken:').split()
        self.cgpa = float(input('Enter cgpa:'))
    
    def printDetails(self):
        super().printDetails()
        print('\nStudent courses: ', self.courses)
        print('\nStudent CGPA: ', self.cgpa)


s1 = JEE()
s1.getMarks()
s1.printDetails()

s2 = Semester()
s2.getSemDetails()
s2.printDetails()        
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:46:36 2022

@author: ajit
"""

import operator
student = { 'ma21m003': {'name':'Ajit', 'CGPA':9, 'Gpa':[9,9,9,9]},
            'ma21m007': {'name': 'Auro', 'CGPA':8.6, 'Gpa':[8,8,9.2,9.2]},
            'ma21m024': {'name':'Sandy','CGPA':9.5, 'Gpa':[9,9,10,10] }
           } 

print('\nGiven dictionary:')
print(student)

# a) Sort the dictionary with respect to CGPA

tempStudent = {}

for roll in student:
    tempStudent[roll] = student[roll]['CGPA']

tempStudent = sorted(tempStudent.items(), key = operator.itemgetter(1))

newStudent = {}

for roll,val in tempStudent:    
    newStudent[roll] = student[roll]

print('\nSorted dictionary:')
print(newStudent)

# b) Insert a new element with respect to the sorted dictionary.


rollNo = 'ma21m005'
details = {'name':'April','CGPA':9.2, 'Gpa':[9.4,9.0,9.0,9.4] }

newest = {}
flag = True

for roll in newStudent:
    if flag and details['CGPA']<= newStudent[roll]['CGPA']:
        newest[rollNo] = details
        newest[roll] = newStudent[roll]
        flag = False
    else:
        newest[roll] = newStudent[roll]

print('\nDictionary with the newest element:')
print(newest)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:32:03 2022

@author: ajit
"""
import random

class Department:
    List = ['EE', 'ED', 'ME', 'MA', 'CS']
    def __init__(self, dn = ""):
        self.dname = dn
    
    def __str__(self):
        return self.dname
    
class Faculty:
    def __init__(self, fn = "", dn = ""):
        self.fname = fn
        self.dfname = Department(dn)
        
    def createFacultyList():
        List = ['Jayant', 'Prashant', 'Rahul', 'Ambi', 'Subramanian', 'Neelesh']
        facultyList = []
        
        rand1 = random.sample(range(0,6), 5)
        rand2 = [random.randint(0, 4) for i in range(5)]
        
        for i in range(5):
            facultyList.append(Faculty(List[rand1[i]], Department.List[rand2[i]]))
        
        return facultyList
    
    def __str__(self):
        return f'Faculty name: {self.fname}\nDepartment name: {self.dfname}'

class Student:
    
    def __init__(self, sn = "", dn = ""):
        self.sname = sn
        self.dsname = Department(dn)
    
    def createStudentList():
        List = ['Ajit', 'Ajay', 'Samyak', 'Deepu', 'Royal', 'Smriti', 'Tang', 'Rajat']
        studentList = []
        
        rand1 = random.sample(range(0,8), 5)
        rand2 = [random.randint(0, 4) for i in range(5)]
        
        for i in range(5):
            studentList.append(Student(List[rand1[i]], Department.List[rand2[i]]))
        
        return studentList
    
    def __str__(self):
        return f'Student name: {self.sname}\nDepartment name: {self.dsname}'

class Derived(Department, Faculty, Student):
    directory_stud = {'EE':set(), 'ED':set(), 'MA':set(), 'CS':set(), 'ME':set()}
    directory_faculty = {'EE':set(), 'ED':set(), 'MA':set(), 'CS':set(), 'ME':set()}

    def __init__(self, d, f, s):
        Department.__init__(self, d.dname)
        Faculty.__init__(self, f.fname, f.dfname)
        Student.__init__(self, s.sname, s.dsname)
        
        Derived.directory_stud[d.dname].add(s.sname)
        Derived.directory_faculty[d.dname].add(f.fname)
    
    def printLists(depName):
        f1 = Faculty.createFacultyList()
        s1 = Student.createStudentList()
        
        print('\nFaculty names and departments:')
        [print(faculty) for faculty in f1]
        
        print('\nStudent names and departments:')
        [print(student) for student in s1]
        
        for faculty in f1:
            for stud in s1:
                if(faculty.dfname.__str__() == stud.dsname.__str__()):
                    Derived(faculty.dfname, faculty, stud)
        
        print('-------------------------------')
        print('Student(s):',Derived.directory_stud[depName])
        print('Teacher(s):',Derived.directory_faculty[depName])
        print('-------------------------------')
        
# Name of the department.
dept = 'EE'
print(dept, 'Department')
Derived.printLists(dept)







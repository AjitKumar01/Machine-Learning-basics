#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 15:35:07 2022

@author: ajit
"""

mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,1,1], [2,2,2],[3,3,3]]

print('Matrix 1:', mat1)
print('Matrix 2:', mat2)

# a)Transpose

# Using list comprehension
transMat = [[row[k] for row in mat1] for k in range(3)]
print('\nTranspose of first matrix: ',transMat)

transMat = [[row[k] for row in mat2] for k in range(3)]
print('Transpose of second matrix: ',transMat)

# Using zip
print('\nUsing Zip:')
ite = zip(*mat1)
print(*ite)

ite = zip(*mat2)
print(*ite)

# b)Addition
        
addMat = [[mat1[i][j] + mat2[i][j] for j in range(3)] for i in range(3)] 

print('\nAddition of matrices:\n', addMat)

# Using zip
ite = zip(mat1,mat2)

ls = list(ite)
 
addMat = [[ls[k][0][i]+ls[k][1][i] for i in range(3)] for k in range(3)]

print(addMat)

# c)Subtraction
        
subMat = [[mat1[i][j] - mat2[i][j] for j in range(3)] for i in range(3)] 

print('\nSubtraction of matrices:\n', subMat)

# Using zip
ite = zip(mat1,mat2)

ls = list(ite)
 
subMat = [[ls[k][0][i]-ls[k][1][i] for i in range(3)] for k in range(3)]

print(subMat)

# d)

# Using list comprehension
    
traceMat = sum([mat1[i][i] for i in range(3)]) 

print('\nTrace of matrix 1:', traceMat)

traceMat = sum([mat2[i][i] for i in range(3)]) 

print('\nTrace of matrix 2:', traceMat)

# Using zip
ite = zip(*mat1)
lst = list(ite)
traceMat = sum([lst[i][i] for i in range(3)]) 

print('\nTrace of matrix 1:', traceMat)

ite = zip(*mat2)
lst = list(ite)
traceMat = sum([lst[i][i] for i in range(3)]) 

print('\nTrace of matrix 1:', traceMat)

 
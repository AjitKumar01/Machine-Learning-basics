#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:49:37 2022

@author: ajit
"""

# iterchange rows
mat1 = [[1,2,3], [4,5,6],[6,7,8]]
mat2 = [[1,1,1], [2,2,2], [3,3,3]]

num = 1    # rows to be interchanged.

ite = zip(mat1, mat2)

lst = list(ite)
lst = [list(i) for i in lst]
lst[num][0],lst[num][1] = lst[num][1],lst[num][0]

mat1 = [lst[i][0] for i in range(3)]
mat2 = [lst[i][1] for i in range(3)]

print('Matrices with interchanged rows:')
print(mat1)
print(mat2)

# interchange columns
mat1 = [[1,2,3], [4,5,6],[6,7,8]]
mat2 = [[1,1,1], [2,2,2], [3,3,3]]

mat1 = [[row[k] for row in mat1] for k in range(3)]
mat2 = [[row[k] for row in mat2] for k in range(3)]

num = 1    # columns to be interchanged.

ite = zip(mat1, mat2)

lst = list(ite)
lst = [list(i) for i in lst]
lst[num][0],lst[num][1] = lst[num][1],lst[num][0]

mat1 = [lst[i][0] for i in range(3)]
mat2 = [lst[i][1] for i in range(3)]

mat1 = [[row[k] for row in mat1] for k in range(3)]
mat2 = [[row[k] for row in mat2] for k in range(3)]

print('\nMatrices with interchanges columns:')
print(mat1)
print(mat2)


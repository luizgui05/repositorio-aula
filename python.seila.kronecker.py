# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:15:36 2019

@author: 42895538859
"""

import numpy as np 

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2,3,4],[5,6,7,8]])

m,n = A.shape
p,q = B.shape

K = np.zeros((m*p, n*q))

for i in range(m):
    for j in range(n):
        K[i*p:(i+1)*p, j*q:(j+1)*q] = A[i,j]*B

print('o produto de kronecker é')
print(K)
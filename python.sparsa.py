# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:40:49 2019

@author: 42895538859
"""

import numpy as np

A = np.array([[1,0,-1,0,0,2,0,1],
              [0,0,1,0,3,0,0,1],
              [1,0,0,0,1,0,0,0],
              [0,5,0,1,0,0,0,-2],
              [0,0,0,1,0,0,0,0],
              [0,0,1,0,2,0,0,-1],
              [0,0,-2,-1,-1,0,0,0],
              [1,0,0,0,0,1,0,0]])

m,n = A.shape

B = np.random.rand(8,8)

p,q = B.shape

#C = np.dot(A,B)

C = np.zeros((m,n))

#for i in range(m):
#    for j in range(n):
#        for k in range(n):
#            C[i,j] = C[i,j] + A[i,k]*B[k,j]
#        
#print(np.allclose(C, np.dot(A,B)))
#
#print(np.max(C-np.dot(A,B)))        


rows,cols = A.nonzero()

#for k in range(m):
     #C[k,:] = A[k,:]@B
#for w in range(m):
#    for k in range(m):
#        somam = 0
#        for j in range(q):
#            if w != rows[j] or j != cols[j]:
#                soma = 0
#            else: 
#                soma = A[w,j]*B[j,k]
#            somam = soma + somam
#            soma = 0
#            C[w,k] = somam
     
#AB = np.zeros((m,q))
#for i in range(m):
#    for j in range(q):
#        for k in range(n):
#            if i in rows and k in cols:
#                AB[i,j] = AB[i,j] + A[i,k]*B[k,j]
#                print('for i={}, j={}, k={}',format(i,j,k))
#                print('we have A{i},{})
            
            
AB = np.zeros((m,q))
for i in range(m):
    for j in range(q):
        for k in range(n):
            if i in rows and k in cols:
                AB[i,j] = AB[i,j] + A[i,k]*B[k,j]
                
            
           
            


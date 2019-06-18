# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 07:50:21 2019

python ama o usuário


@author: 42895538859
"""

import scipy.linalg as sp
import numpy as np

A = np.array([[1,3,5],
              [4,1,3],
              [7,6,7]])

B = np.array([[1,4,5],
              [5,3,8],
              [6,3,2]])

v = np.array([[3],
              [2],
              [1]])
c = np.array([[0],
              [0],
              [0]])

m,n = A.shape

p,q = B.shape

z = np.zeros((m,q))

soma = 0
somam = 0
#for i in range(m):
    #for k in range(n):
        #soma = B[i][k]*v[k]
#        somam = soma + somam
#        soma = 0
#    c[i] = somam
#    somam = 0
    
#Tarefa 3 dia 30/04   
    
#for k in range(q):
#    z[:,k] = np.dot(A,B[:,k])
    
for k in range(m):
     z[k,:] = A[k,:]@B
for w in range(m):
    for k in range(m):
        somam = 0
        for j in range(q):
            soma = A[w,j]*B[j,k]
            somam = soma + somam
            soma = 0
        z[w,k] = somam
        
            
        
    
    
        

    

    





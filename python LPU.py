# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""


import time

import scipy.linalg as sp
import numpy as np

#print(sp.__doc__)

#print(sp.inv.__doc__)

# array_like listas vetorees duplas ordenadas...  bool logica booliana, com verdadeiro e falso
# verwrite_a : bool, optional Discard data in `a` (may improve performance) pega a matriz deleta
 

A = np.array([[1,2,3],
     [4,5,6],
     [7,8,9]])



Ainv = sp.inv(A)

A1 = np.array([[1,10001],
      [1,1]])
A2 = np.array([[1,1],
      [1,1]])

b = np.array([[1],
     [1]])

c = np.array([[1.0001],
              [1]])

x = sp.solve(A1,b)

 #solve so resolve quadradas 
b1 = np.array([[1],
               [1.0001]])
x1 = sp.solve(A1,b1)

P, L, U = sp.lu(A1)

y = sp.solve(P@L,b)
x = sp.solve(U,y)


yc = sp.solve(P@L,c)
xc = sp.solve(U,yc)

A = np.random.rand(5000,5000)
b = np.random.rand(5000,)

#t0 = time.time()
#xinv = sp.inv(A)@b
#print(time.time() - t0)

t0 = time.time()
sp.solve(A,b)
print(time.time() - t0)
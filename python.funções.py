# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:02:50 2019

python ama o usuário

@author: 42895538859
"""

import numpy as np

import math

import matplotlib.pyplot as plt


def quadrado(x): 
    return x**2 

#METODO DA BISSECÇÃO

def f(x):
    return x**2 - np.pi
      
def bissecção(f,a,b,tolerancia=1e-10):
    if np.abs(f(a)) <= tolerancia:
        return a
    elif np.abs(f(b)) <= 0:
        return b
    elif f(a)*f(b) > 0:
        return np.Inf
    else:
        x = (a+b)/2
        print("x = {}".format(x))
        print("f(x) = {}".format(f(x)))
        nbiter = 0
        while np.abs(f(x)) >= tolerancia:
             if f(x)*f(a) > 0:
                 a = x
             else:
                 b = x
             x =(a+b)/2
             print("x = {}".format(x))
             print("f(x) = {}".format(f(x)))
             nbiter = nbiter +1
        return x, nbiter     

def g(x):
    return x

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        xk = 1
        while n != 1:
            x = g(n)
            n = n - 1
            xk= x*xk
        return xk    
            
        
          
          

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 07:51:59 2019

python ama o usuário

@author: 42895538859
"""
import numpy as np

import math

import matplotlib.pyplot as plt

x = np.linspace(0,23,20000)

y = np.exp(x*np.log(np.cos(math.factorial(14)*x)))
#soma = 0
#somam = 0
#for k in range(200):
#    soma = np.cos(k*(x+11)) + np.sin(k*(x+11)) 
#    somam = soma + somam
#y = somam*(1/200)     
#
#plt.xlabel('hora do dia')
#plt.ylabel('fome')
#plt.title('fome ao decorrer do dia $x^2+\cos{x}$')
#
#
print(plt.plot(x,y))

#fig, axes = plt.subplots()
#pontos = [1,3,2,7,5,9,4]
#axes.plot(pontos, 'b',linestyle='dotted')
#axes.plot(pontos, 'y*', markersize=20)
#axes.axis([-1,8,0,10])
#plt.show()

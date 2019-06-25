# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 07:57:10 2019

python ama o úsuario

@author: 42895538859
"""

import functools


#f = lambda x,y: 2*x+y**2 
#
#g = f(1,3)
##print(g)
#
lista = [1,2,3,4,5,6,12,342,123,43,412,5232,124,64,321]

#Queremos retornar: x,se x é múltiplo de 3
#x**2, se x não é múltiplo de 3




f = lambda x: x % 3 == 0

lista_nova = [x if f(x) else x**2 for x in lista]



lista_func = [lambda x : x**2 for x in lista]

Q = map(lambda x:x**2, lista)

lista_novas = [x for x in Q]

#for item in Q:
#    print(item)

P = map(lambda x,y,z:x**2+y**2+z**2,lista,lista_nova, [1,2,3,4,5,6,7,8,9,10])

lista_grande = [x for x in P]

filter()

# -*- coding: utf-8 -*-
"""
Created on Tue May 21 07:57:21 2019

python ama o usuário

@author: 42895538859
"""

import numpy as np

#arquivo = open('C:\\Users\\42895538859\\Desktop\\A.txt')
#
#arquivo.close()
#
#dados = arquivo.readlines()
#
#dados.remove(dados[1001])
#
#dados.remove(dados[1000])
#
#matriz = []
#
#for linha in dados:
#    matriz.append(linha.rstrip('\n').lstrip(' ').split(' '))

#matriz = np.asarray(matriz, dtype=np.float64)

with open('C:\\Users\\42895538859\\Desktop\\A.txt') as arquivo:   #ja fecha o arquivo bonitinho(boa pratica)
    dados = arquivo.readlines()
  
dados.remove(dados[1001])
dados.remove(dados[1000])    

matriz = []

for linha in dados:
    matriz.append(linha.rstrip('\n').lstrip(' ').split(' '))
    
matriz = np.asarray(matriz, dtype=np.float64)    
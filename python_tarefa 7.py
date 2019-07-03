# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:44:22 2019

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

with open('C:\\Users\\42895538859\\Desktop\\B.txt') as arquivo_b:
    dados_b = arquivo_b.readlines()
    
matriz_b = []

pode_ler = False 
    
for linha in dados_b:
    if pode_ler:
        matriz_b.append(linha)
   # print(linha[0])    
    if 'columns' in linha:
           pode_ler = True

matriz_B = []

for linha in matriz_b:
     matriz_B.append(linha.rstrip('\n').lstrip(' ').split(' '))
     

del matriz_B[500:] 
    

matriz_B = np.asarray(matriz_B, dtype=np.float64)         
                        
m,n = matriz.shape
p,q = matriz_B.shape

A = matriz
B = matriz_B

K = np.zeros((p,q))

#for i in range(m):
#    for j in range(n):
#        K[i*p:(i+1)*p, j*q:(j+1)*q] = A[i,j]*B

lista = []
for i in range(m):
    K = A[0,i]*B 
    lista.append(K)

#print('o produto de kronecker é')
#print(K)

            
        
    
    
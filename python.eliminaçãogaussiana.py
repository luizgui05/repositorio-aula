# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:23:07 2019

python ama o usuário

@author: 42895538859
"""

import numpy as np

# Eliminação Gaussiana com permutação generalizada: P*A = L*U - A retangular (m x n);
# n: número de linhas;
# m: Número de colunas.
# Pe := np.array(n); # l-ésima matriz de permutação;

'Outputs'


# P := np.array(n); # Matriz de permutação no estágio final da Eliminação;
# L := np.array(n); # Matriz triangular inferior dos fatores;
# U := np.array(1..n,1..n); # Matriz triangular superior dos fatores, no estágio final da eliminação

def G_el(X):
    # Cria a matriz de saída U (m x n).
    U = np.array(X, dtype=float)

    # Defini-se as dimensões m e n da matriz.
    (n, m) = U.shape

    # Geração das matrizes de saída P e L, onde P é matriz de permutação e L matriz das transformaçõe elementares.
    L = np.eye(n)
    P = np.eye(n)

    # k varia sobre as colunas de U, buscando seus pivôs.
    for k in range(m):

        # Se um de seus pivôs for zero, procura-se na mesma coluna um índice i de modo que
        # o elemento de U correspondente seja diferente de 0. Aplica-se então uma troca de linhas afim de defini-lo
        # como novo pivô.
        if U[k, k] == 0:
            Pe = np.eye(n)
            i = k
            while U[i, i] == 0:
                i += 1
            # Troca de linhas:
            p1 = np.array(P[i, :])
            p2 = np.array(P[k, :])
            Pe[i, :] = p2
            Pe[k, :] = p1
            U = np.dot(Pe, U)
            P = np.dot(Pe, P)
        # Caso não haja elemento nulo no candidato à pivô, continuamos normalmente:
        else:
            # simplificando a linha do pivô, afim de transforma-lo em 1.
            a = U[k, k]
            L[k, k] = a
            U[k, :] = U[k, :] * (1 / a)

            # Zerando os elementos abaixo do pivô, e subtraindo a linha do pivô das demais linhas abaixo.
            for i in range(k + 1, n):
                b = U[i, k]
                L[i, k] = b
                U[i, :] = U[i, :] - b * U[k, :]

    return P, L, U


A = [[3, 5, 7], [1, 2, 3], [7, 9, 1]]
(P, L, U) = G_el(A)

print(A)

print(P)

print(L)

print(U)

print(np.dot(P, np.dot(L, U)))

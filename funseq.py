#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 00:04:36 2018

@author: mejnour
"""
# Declara listas
s = []
q = []
w = []

# Popula s
aux = input()
s = input().split()

# Popula q
aux = input()
q = input().split()

# Processa elementos que estão em s e nao em q
for i in range(len(s)):
    
    # Compara elementos de s com todos de q
    # Quando forem diferentes, conta 1
    aux = 0
    for j in range(len(q)):
        if s[i] == q[j]:
            continue
        else:
            aux += 1
            
    # Se o contador for do tamanho de q,
    # quer dizer que todos os testes fo-
    # ram feitos e nenhum passou.
    if aux == len(q):
        w.append(s[i])

# Imprime a resposta
for k in w:
    print(k, end = " ")
print("\n")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 02:13:14 2018

@author: mejnour
"""

class Stack:
    def __init__(self):
        self.items = []
        self.size = 0
        
    def length(self):
        return self.size
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def push(self, item):
        self.items.append(item)
        self.size += 1
        
    def pop(self):
        self.items.pop()
        self.size -= 1

str1 = []        
qtd = input()

# Quantidade de testes
for i in range(int(qtd)):
    aux2 = input()
    length = len(aux2) + 1
    
    # Loop para cada teste
    pilha = Stack()
    x = 0
    aux1 = []
    for j in range(1, length):
        # Quando é 0, é mais seguro deixar ciclar        
        if aux2[x:j] == '(':
            pilha.push('(')
            
        elif aux2[x:j].isalpha():
            aux1.append(aux2[x:j])
            
        elif aux2[x:j] == '^':
            
            while pilha.peek() == '^':
                aux1.append(pilha.pop())
                
            pilha.push(aux2[x:j])
            
        elif aux2[x:j] == '*' or aux2[x:j] == '/':
            
            while pilha.peek() == '*' or pilha.peek() == '/' or pilha.peek() == '^':
                aux1.append(pilha.pop())
            
            pilha.push(aux2[x:j])
            
        elif aux2[x:j] == '+' or aux2[x:j] == '-':
        
            while pilha.peek() != '(':
                aux1.append(pilha.pop())
                
            pilha.push(aux2[x:j])
            
        elif aux2[x:j] == ')':

            while pilha.peek() != '(':
                aux3 = pilha.peek()
                aux1.append(aux3)
                pilha.pop()
                
            pilha.pop()
            
        x += 1
    
    str1.append(''.join(aux1))
    str1.append('')
        
for k in str1:
    print(k)
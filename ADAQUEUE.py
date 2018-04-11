#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 00:06:30 2018

@author: mejnour
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class No:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    def setPrev(self, prev):
        self.prev = prev
        
    def getPrev(self):
        return self.prev
    
class Queue:
    def __init__(self):
        self.head = No(None)
        self.tail = No(None)
        self.size = 0
        self.reversed = False
        
    def reverse(self):
        if self.size == 0:
            return
        
        aux = self.tail
        self.tail = aux
        if self.reversed:
            self.reversed = False
        else:
            self.reversed = True
        
    def pushFront(self, cmdAux):
        sec = int(cmdAux)
        novoNo = No(sec)
        
        if self.reversed == True:
            self.reverse()
            self.pushBack(cmdAux)
            self.reverse()
            
        else:
            if self.size == 0:
                self.head = novoNo
                self.tail = novoNo
            
            else:
                self.head.setPrev(novoNo)
                novoNo.setNext(self.head)
                self.head = novoNo
                
        self.size += 1
        print(self.size)

    def pushBack(self, cmdAux):
        sec = int(cmdAux)
        novoNo = No(sec)
        
        if self.reversed == True:
            self.reverse()
            self.pushFront(cmdAux)
            self.reverse()
            
        else:
            print(self.reversed)
            if self.size == 0:
                self.head = novoNo
            
            else:
                self.head.setPrev(self.tail)
                self.tail.setNext(novoNo)
                
        self.tail = novoNo
        self.size += 1
        
    def removeFront(self):
        if self.reversed == True:
            self.reverse()
            self.removeBack()
            self.reverse()
            
        else:
            
            if self.size == 0:
                output.append("No job for Ada?")
            
            else:
                aux = self.head.getData()
                p = self.head
                
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    
                else:
                    self.head = p.getNext()
                    p.setNext(None)
                    self.head.setPrev(None)
                
                p = None
                self.size -= 1
                output.append(aux)
                print(self.size)
        
    def removeBack(self):
        if self.reversed == True:
            self.reverse()
            self.removeFront()
            self.reverse()
        else:
            if self.size == 0:
                output.append("No job for Ada?")
            
            else:
                aux = self.head.getData()
                p = No(self.tail)
                
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    
                else:
                    self.tail = p.getPrev()
                    self.tail.setNext(None)
                
                p = None
                self.size -= 1
                output.append(aux)
        
    def command(self, cmd):
        cmdAux = []
        cmdAux = cmd.split()
        
        if cmdAux[0] == 'back':
            self.removeBack()
        
        elif cmdAux[0] == 'front':
            self.removeFront()
        
        elif cmdAux[0] == 'push_back':
            self.pushBack(cmdAux[1])
            
        elif cmdAux[0] == 'toFront':
            self.pushFront(cmdAux[1])
            
        elif cmdAux[0] == 'reverse':
            self.reverse()

output = []
fila = Queue()    
length = input()
for i in range(int(length)):
    inputCmd = input()
    fila.command(inputCmd)
    
for j in output:
    print(j)
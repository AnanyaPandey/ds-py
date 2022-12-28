#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 13:22:09 2022

@author: ananyapa

LinkedList Practice Questions 
"""
from random import randint

class Node :
    def __init__(self,val):
        self.value = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class Linkedlist :
    def __init__(self,val=None):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' '.join(values)
    
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result +=1
            node = node.next
        return result
    
    def add(self,val):
        if self.head == None:
            node = Node(val)
            self.head = node
            self.tail = node
        else : 
            self.tail.next = Node(val)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self,n,minval,maxval): # generate node wirh rand value
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(minval,maxval))
        return self
    
    # ----- Uncomment Below code can be used to check the program ----
#newList = Linkedlist()
#newList.generate(10, 0, 99) 
#print(newList)
#print(len(newList))
       
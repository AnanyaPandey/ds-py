#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 12:21:56 2022

@author: ananyapa
Queues : 
    Consider infinite size python list queue.
    
"""

class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == [] :
            return True
        else : 
            return False
    def enqueue(self,val): # O(n) time complexity
        self.items.append(val)
        return 'element added'
    
    def dequeue(self): 
        if self.isEmpty():
            return 'Queue empty'
        else :
            return self.items.pop(0) 
            # O(n) Complexity needs to shift all elements
    
    def front(self):
        if self.isEmpty() :
            return 'list empty'
        else : 
            return self.items[0]
    def deleteQ(self):
        self.items = None
        
Q1 = Queue()
Q1.enqueue(11)
Q1.enqueue(12)
Q1.enqueue(14)
Q1.enqueue(17)
Q1.enqueue(19)
Q1.enqueue(21)
print(Q1)
Q1.dequeue()
print(Q1)

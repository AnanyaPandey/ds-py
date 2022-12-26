# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:33:50 2022

@author: pandey
Stack of books
Stack of plates
Last in First Out
Stack Operations : 
    CreateStack
    Push (insert)
    Pop (delete)
    isEmpty
    DeleteEntireStack
    isfull
    peek - check last (top) element (LIFO)
(back button in browser) e.g. of Stack
# we can ceate stack using other data structure like arrays list or linkedlists
# takes advantage of spatial locaity

Advanage : 
    Implementation is easy
    
Disadvantage :
    Speed issue when size grows    
Implemented using list  : 
    easy to implement
    speed isssue 
Implemeted using linkedist
    Fast performance
    difficult to implement

Memory allocation as per the underlying data structure
"""

# implementation using numpy array or list

# Creating the Stack
import numpy as np
class stack:
    def __init__(self,size):
        self.list = []
        self.maxsize=size
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    def isempty(self):
        if self.list == [] :
            return True
        else : 
            return False

    def push(self,item):
        if self.isfull():
            return 'list full'
        else :   
            self.list.append(item) # list creates space more than actual no.
            return 'item added'
        
    def pop(self):
        if self.isempty() :
            return 'empty list'
        else :
            return self.list.pop()
    
    def top(self):
        if self.isempty():
            return 'list empty'
        else :
            return self.list[-1]
    
    def isfull(self):
        if len(self.list) == self.maxsize :
            return True
        else : 
            return False
    def delstack(self):
        self.list.clear()

s1 = stack(10)
s1.isempty()
s1.push(22)
s1.push(33)
s1.push(44)
s1.push(55)
print(s1)
s1.pop()
print(s1)
s1.top()
s1.delstack()
print(s1)
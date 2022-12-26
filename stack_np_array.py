# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:32:36 2022

@author: pandey
Stacks using numpy ararys 
"""

import numpy as np
class stack:
    def __init__(self,size):
        self.maxsize = size
        self.array = np.array([])
    
    def __str__(self):
        return str(self.array)
    
    def isempty(self):
        if len(self.array) == 0 :
            return True
        else : 
            return False

    def push(self,item):
        if self.isfull():
            return 'list full'
        else :   
            self.array = np.append(self.array,item) # list creates space more than actual no.
            return 'item added'
            
    def pop(self):
        if self.isempty() :
            return 'empty list'
        else :
            self.array = np.delete(self.array,-1)
            return self.array
    
    def top(self):
        if self.isempty():
            return 'list empty'
        else :
            print(self.array[-1])
    
    def isfull(self):
        if len(self.array) == self.maxsize :
            return True
        else : 
            return False
    def delstack(self):
        self.array = np.empty(0)
        

s1 = stack(10)
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

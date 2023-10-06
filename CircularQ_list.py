#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 12:43:05 2022

@author: ananyapa
Circular Queue using List. 

"""
class Cqueue :
    def __init__(self,size):
        self.items = size*[None] # O(n)
        self.maxsize = size
        self.start = -1
        self.end = -1
        # -1 will indicate empty list or blank list
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isfull(self):
        if self.end +1 == self.start :
            return True
        elif self.start == 0 and self.end == self.maxsize-1 :
            return True
        else : 
            return False
        
    def isEmpty(self):
        if self.end == -1:
            return True
        else : 
            return False

    def enqueue(self,val):
        if self.isfull():
            return 'list full'
        else : 
            if self.end + 1 == self.maxsize :
                self.end = 0 
            else : 
                self.end += 1
                if self.start == -1: # list is empty
                    self.start = 0
        self.items[self.end] = val
    
    def Cenqueue(self,val):
        if self.isfull() :
            return 'list full'
        else : 
            if self.start == self.end == -1 : # check if empty
                self.start = 0
                self.end = 0
            else : 
                if self.end +1 == self.maxsize :
                    self.end = 0 
                else : 
                    self.end +=1 
            self.items[self.end] = val
            print('element inserted')
            
    def Cdequeue(self): # Time complexity is O(1)
        if self.isEmpty() :
            return 'list empty'
        else :
            # first update the pointer then update list at that pointer
            # Also in Dequeue we have to move all item forward
            firstelement = self.items[self.start]
            start = self.start
            if self.start == self.end : 
                # only 1 element 
                self.start = -1
                self.end = -1
            elif self.start +1 == self.maxsize: # start at end of list
                self.start = 0
            else : 
                self.start +=1
            self.items[start] = None
            return firstelement
                
    def front(self):
        if self.isEmpty() :
            return 'list empty'
        else : 
            return self.items[self.start]

    def deleteQ(self):
        self.items = None
        self.start = -1 
        self.end = -1               
    
    def deleteQueue(self):
        self.start = -1
        self.top = -1
        self.list = [None] * self.maxSize
 
    def printQueue(self):
        values = []
        for i in range(self.start, self.maxsize):
            x = self.items[i]
            if x:
                values.append(self.items[i])
        for i in range(0, self.start):
            x = self.items[i]
            if x:
                values.append(self.items[i])
        print(values)
            
CQ1 = Cqueue(4)
print(CQ1)

print(CQ1.isfull())
print(CQ1.isEmpty())
CQ1.Cenqueue(21)
CQ1.Cenqueue(23)
CQ1.enqueue(51)
CQ1.Cenqueue(71)
print(CQ1)

CQ1.printQueue()
CQ1.Cdequeue()
CQ1.Cdequeue()
CQ1.Cenqueue(11)
CQ1.enqueue(22)
CQ1.printQueue()


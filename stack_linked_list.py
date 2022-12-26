# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:50:36 2022

@author: pandey
# Stacks using linkedlist 
we use a linkedlist instead of a normal list to enhance performance
# to push we alwasys push element as first node 
# to pop we always pop the first eement onf the list
# head always points to the top node
# linear linkedist is good eneough
"""

class Node :
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Linkedlist :
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class stacks:
    def __init__(self):
# when we are creating stack we are automatically creating a linkedlist
        self.linkedlist = Linkedlist()

    
    def __str__(self):
        values = [str(x.value) for x in self.linkedlist]
        return ' '.join(values)
    
    def isempty(self):
        if self.linkedlist.head == None : 
            return True
        else : 
            return False
    def push(self,value):
        node = Node(value) # new node create
        node.next = self.linkedlist.head # nodes next is current head
        self.linkedlist.head = node # head's next points to node
        # pushing new node as first point 
        
    def pop(self):
        if self.isempty():
            return 'list is empty'
        else:
            nodevalue = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return nodevalue
    
    def top(self):
        if self.isempty():
            return 'list empty'
        else:
            nodevalue = self.linkedlist.head.value
            return nodevalue
    
    def deletestack(self):
        self.linkedlist.head = None
        
            
        
stack1 = stacks()
stack1.push(22)
stack1.push(33)
stack1.push(55)

print(stack1.isempty())
print(stack1)
stack1.pop()
print(stack1)
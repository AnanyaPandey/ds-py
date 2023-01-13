#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:43:41 2021

@author: ananyapa
Queues : using linked lists
When no one reference to a node X the node X gets garbage collected.
"""

class Node:
    def __init__(self,val=None):
        self.value = val
        self.next = None
        
    def __str__(self):
        return(str(self.value))
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node is not None :
            yield node
            node = node.next
    
class Queue:
    
    def __init__(self):
        self.linkedlist = LinkedList()
    
    def __str__(self):
        val = [str(x) for x in self.linkedlist]
        return ' '.join(val)
   
    def enqueue(self,item):
        node = Node(item)
        if self.linkedlist.head == None : 
            self.linkedlist.head = node
            self.linkedlist.tail = node
        
        else :
            self.linkedlist.tail.next = node
            self.linkedlist.tail = node
            
    def dequeue(self):
        if self.linkedlist.head == None:
            return 'List is empty'
        elif self.linkedlist.head == self.linkedlist.tail:
            self.linkedlist.head = None
            self.linkedlist.tail = None
        else :
            temp = self.linkedlist.head
            self.linkedlist.head = temp.next

    def isEmpty(self):
        return self.linkedlist.head == None
    
    def front(self):
        if self.isEmpty():
            return 'List is empty'
        else:
            return self.linkedlist.head # returns a node.
    
    def deleteQ(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None
    
Q1= Queue()
Q1.enqueue(12)
Q1.enqueue(21)
Q1.enqueue(31)
Q1.enqueue(13)
Q1.enqueue(34)
Q1.enqueue(36)
print(Q1)
Q1.dequeue()
print(Q1)
print('front item ',Q1.front())

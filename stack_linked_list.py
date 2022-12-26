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

class stacks:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        node = self.head
        while node is not None : 
            node = node.next
            p = ''.join(node.value)
        return p
    
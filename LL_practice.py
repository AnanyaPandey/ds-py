#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 14:32:43 2022

@author: ananyapa
"""

from Linkedlist_practice import *


def removeduplicates(ll):
    '''
    Basically find the duplicates and remove that node from the linkedlist
    Consider unsorted Single Linked list
    This ia done by maintaining a temporary set. set is used because set
    has only unique values. Check if current node is in set. 
    '''
    if ll.head == None :
        return 'empty list'
    else : 
        node = ll.head
        temp = set([node.value]) # adding existing node value to set
        while node.next is not None: 
            if node.next.value in temp : 
                node.next = (node.next).next
            else : 
                temp.add(node.next.value)
                node = node.next
        return ll
print('Program to remove duplicate from the linked list')
newll = Linkedlist()
newll.generate(15, 0, 20)
print(newll)
removeduplicates(newll)
print(newll)                
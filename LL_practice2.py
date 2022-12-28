#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:14:05 2022

@author: ananyapa
Find Nth element from the last node for Single Linked List
Two methods 
1. Iterative
2. Reccursive
We dont know the linkedlist length so we have two pointers kept at n 
distance apart, p1 start from start and p2 starts from n gap when p2 reaches
end p1 will be at the node nth from the last. So we remove node at p1

"""
print('Find the Nth element from the last of linkedlist')
from Linkedlist_practice import * 

def NthtoLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head
    for i in range(n):
        if pointer2 == None : 
            return None
        pointer2 = pointer2.next
    # Now both are n distance apart. 
    
    while pointer2 is not None : 
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1

newll = Linkedlist()
newll.generate(10, 0, 20)
print(newll)
print(NthtoLast(newll, 5))
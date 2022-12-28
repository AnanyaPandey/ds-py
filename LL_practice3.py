#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:26:17 2022

@author: ananyapa
Partition the linkedlist around value X such that all values before X are 
less than X and values greater of equal to X come after X.
Add N digit number represented by linked lists in reverse
"""


from Linkedlist_practice import *

def sumlist(lla,llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0 
    ll = Linkedlist()
    while n1 or n2 : 
        result = carry
        if n1 : 
            result += n1.value
            n1 = n1.next
        if n2: 
            result += n2.value
            n2 = n2.next
        ll.add(int(result%10))
        carry = result /10
    return ll

llA = Linkedlist()
llB = Linkedlist()
llA.add(2)
llA.add(4)
llB.add(7)
llB.add(9)
print(sumlist(llA,llB))        
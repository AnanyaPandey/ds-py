#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:55:02 2022
@author: ananyapa

Intersection of two single linked list. Intersection based on reference 
and not on value. Given intersection is of a Y type which means head is
same but tail is definitely same.
"""

from Linkedlist_practice import * 

def Yintersection(ll1,ll2):
    if ll1.tail is ll2.tail :
        return True
    
    lenA = len(ll1)
    lenB = len(ll2)

    shorter = ll1 if lenA < lenB else ll2
    longer = ll1 if lenA > lenB else ll2
    
    diff = len(longer) - len(shorter)
    longernode = longer.head
    shorternode = shorter.head
    
    # once we cover the extra length then we can traverse both together
    for each in range(diff):
        longernode = longernode.next
    
    while shorternode is not longernode:
        shorternode = shorternode.next
        longernode = longernode.next
    
    return shorternode

# Code to check the intersection. WE have to create intersected LL
# This will add same value but different nodes 
def addsamenode(lla,llb,value):
    tempnode = Node(value)
    lla.add(tempnode)
    llb.add(tempnode)

def addintersectingnode(lla,llb,value):
    node = Node(value)
    lla.tail.next = node
    lla.tail = node
    llb.tail.next = node
    llb.tail = node

lla = Linkedlist()
llb = Linkedlist()
lla.generate(4, 0, 20)
llb.generate(6, 20, 40)

addsamenode(lla,llb,51)
addsamenode(lla,llb,52)
print(f'list A {lla}')
print(f'list B {llb}')
print(Yintersection(lla,llb))
print('adding intersecting node')
addintersectingnode(lla,llb,71)
addintersectingnode(lla,llb,72)
addintersectingnode(lla,llb,73)
print(f'list A {lla}')
print(f'list B {llb}')
print(Yintersection(lla,llb))


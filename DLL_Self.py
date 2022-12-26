# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:16:39 2022

@author: pandey
============= EXPERIMENT PURPOSE =================
Double liinkedlist
any node reference to previous and next node
 making reverse traversal also possible
 
 Create a node
 point hea to node point tail to node
 point node to previous, point node to next

each node has two parameter other than value
1. previous
2. next
 
Insertion process
1. Create a blank node, assign it value
2. Check the location where it needs to be inserted
3. BEGINING : 
    3.1 nodes next reference point to heads next
        3.1.1 (2nd node) Head;s next;s previous point to newly crtead node
    3.2 hed points to new created node.
    3.3 nodes previous points to head
4. MIDDLE : 
    4.1 traverse to location -1
    4.2 link new node next = locationnode
    4.3 link new node prev = location -1 (current node)
    4.4 Current nodes next points to new node
    4.5 location node previous points to new node
5. END : 
    5.1 traveese untill nodes next refrerence -s None.
    5.2 new nodes next = None
    5.3 point new nodes prev to current node
    5.4 current nodes next point to new node.
    5.5 point tail to new node.
 """
class Node:
    def __init__(self,val):
        self.value = val
        self.prev = None
        self.next = None
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setPrev(self,node):
        self.prev = node
    
    def setNext(self,node):
        self.next = node
    
class Dlinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createnode(self,nodeval):
        node = Node(nodeval)
        self.head = node
        self.tail = node
        return "DLL Created"
    
    def insertafter(self,location,val):
        node = Node(val)
        index = 0
        while index < location -1 :
            index+=1
            node = node.next
        node.setPrev(node.next)
        node.setNext(node.next.getNext())
        (node.next.getNext()).setPrev(node)
        node.next.setNext(node)
        return node
        
        

Dll1 = Dlinkedlist()
Dll1.createnode(11)
Dll1.createnode(44)
Dll1.insertafter(0, 77)
print([node.value for node in Dll1])
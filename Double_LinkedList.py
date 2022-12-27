# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:16:39 2022

@author: pandey

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
        if self.head == None : 
            print('list empty creating at 0th location')
            self.createnode(val) # creating node in empty list
        else : 
            newnode = Node(val)
            if location == 0:
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
                newnode.prev = None

            elif location == -1 :
                newnode.next = None
                newnode.prev = self.tail
                self.tail.next = newnode
                self.tail = newnode
            else : 
                tempnode = self.head
                index = 0
                while index < location -1 :
                    tempnode = tempnode.next
                    index += 1
                # currentnode = tempnode
                # we are at the node after which we have to insert new node
                newnode.prev = tempnode
                newnode.next = tempnode.next
                tempnode.next = newnode
                t = tempnode.next
                t.prev = newnode
    def traverseDLL(self):
        if self.head == None : 
            print('list empty')
        else :             
            node = self.head
            while node is not None : 
                print(node.value)
                node = node.next
    def reverseTraverse(self):
        if self.head == None : 
            print('list empty')
        else :
            node = self.tail 
            while node:
                print(node.value)
                node = node.prev
    def searchitemDLL(self,item):
        if self.head == None : 
            return 'list empty'
        else : 
            node = self.head
            while node is not None : 
                if node.value == item : 
                    return f"found value {node.value}"
                else :
                    node = node.next
            return 'Not Found'
    def deletenodeDLL(self,location):
        if self.head == None : 
            return 'list is empty'
        else : 
            if self.head == self.tail :
                self.head = None
                self.tail = None
            else : 
                if location == 0:
                    self.head = self.head.next
                    self.head.prev = None
                    
                elif location == -1 : 
                    self.tail = self.tail.prev
                    self.tail.next = None
                else : 
                    node = self.head
                    index = 0
                    while index < location -1 : 
                        node = node.next
                        index+=1 
                    temp = node.next
                    node.next = temp.next
                    node.next.prev = node
            print('Node deleted')
    
    def deleteentireDLL(self):
        # just by deleting head and tail will not delete list
        # we have to set entire list references to Null 
        # if no node poinst to any node X it gets garbage 
        if self.head == None: 
            return 'empty list'
        else : 
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None
            print('deleted entire list')
                
Dll1 = Dlinkedlist()
Dll1.insertafter(0,22)
Dll1.insertafter(0,99)
Dll1.insertafter(0,33)
Dll1.insertafter(0,77)
Dll1.insertafter(0,88)
Dll1.insertafter(-1, 67)
Dll1.insertafter(-1, 76)
Dll1.insertafter(3, 55)
print(Dll1.head.value)
print(Dll1.tail.value)
print([node.value for node in Dll1])
# Dll1.reverseTraverse()
Dll1.searchitemDLL(99)
Dll1.deletenodeDLL(6)
print([node.value for node in Dll1])
Dll1.deleteentireDLL()
print([node.value for node in Dll1])
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:43:26 2022

@author: ananyapa
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Slinkedlist:
    def __init__(self):
        self.head = None
        self.Tail = None

    # Code to make this data structure ( linked lis iterable)
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # To Insert the node
    def insertnode(self, value, location):
        newnode = Node(value)  # newnode value is set here itself
        if self.head == None:  # no nodeudem exist.
            self.head = newnode
            self.tail = newnode
        elif location == 0:  # 1st position
            newnode.next = self.head
            self.head = newnode
        elif location == -1:  # tail
            newnode.next = None
            self.tail.next = newnode
            self.tail = newnode  # self.<whater> = value self.<node>.next = reference of that node
        else:
            tempnode = self.head  # starting point
            i = 0
            while i < location - 1:
                tempnode = tempnode.next  # traversing to the nth location
                i += 1
            nextnode = tempnode.next  # temp reference
            tempnode.next = newnode  # temonode is the current node while traversing
            newnode.next = nextnode
            if tempnode == self.tail:
                self.tail = newnode
                newnode.next = None

    def traverselinkedlist(self):
        if self.head == None:
            print("Songle Linkedlist is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    def deletenode(self,location):
        if self.head == None : 
            print('list is empty')
        else : 
            if location == 0 :
# if there is only one node we have to handle tail as well. 
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else : 
                    self.head = self.head.next
            
            elif location == -1 : # last node
                if self.head == self.tail : # last is the only node
                    self.head = None
                    self.tail = None
                else : 
                    # traveese to the last node untill we reach tail
                    node = self.head
                    while node is not None : 
                        if node.next == self.tail : 
                            break 
                        node = node.next
                        self.tail = node
            else :
                tempnode = self.head
                ind = 0 
                while ind < location - 1: # before req node
                    tempnode = tempnode.next
                    ind += 1
                nextnode = tempnode.next # pointing to its next ref
                tempnode = nextnode.next
                
            # Basically writing tempnode = tempnode.next.next
                
    def deleteentirelist(self):
        if self.head == None : 
            print('list already empty')
        else : 
            self.head = None
            self.tail = None
            print('deleted the entire list')

class CircularLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node :
            yield node  # jab tak aisa node nahi ata jiska next head hai
            if node.next == self.head : # reached the end 
                break
            node = node.next
    def createCSLLnode(self,nodevalue):
            newnode = Node(nodevalue)
            newnode.next = newnode
            self.head = newnode
            self.tail = newnode
            
    def insertnode(self,location,value):
        if self.head == None : 
            createCSLLnode(value)
        else : 
            newnode = Node(value)
            if location == 0 :
                newnode.next = self.head
                self.head = newnode
                # make last node point newnode
                self.tail.next = newnode
            elif location == -1:
                newnode.next = self.tail.next
                self.tail.next = newnode
                self.tail = newnode
            else : 
                node = self.head
                index = 0
                while nindex < location-1 :
                    node = node.next
                    index += 1
                temp = node.next # temo storing the reference
                node.next = newnode
                newnode.next = temp    
        return "node inserted"
    
    def traverse(self):
        if self.head == None : 
            print('List is empty')
        else : 
            node = self.head
            while True : # condution of being head
                print(node.value)
                node= node.next
                if node == self.tail.next:
                    break

    def searchcsll(self,values):
        if self.head == None : 
            print('List is empty')
        else : 
            node = self.head
            while True : # condution of being head
                if node.value == values:
                    print(f"found at node {node.value} ")
                node= node.next
                if node == self.tail.next:
                    return "not found"                

slist = Slinkedlist()
slist.insertnode(1, 1)
slist.insertnode(2, 1)
slist.insertnode(22, 1)
slist.insertnode(3, 1)
slist.insertnode(4, 1)

print([node.value for node in slist])
slist.traverselinkedlist()
slist.deleteentirelist()
csll1 = CircularLinkedList()
csll1.createCSLLnode(1)
csll1.createCSLLnode(22)
csll1.insertnode(-1, 44)
csll1.insertnode(-1, 23)
csll1.insertnode(0, 12)
csll1.traverse()
csll1.searchcsll(23)
print([node.value for node in csll1])

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:01:44 2023

@author: pandey
STack and Queue Interview Question
Using Single python list to implement 3 Stacks
"""

class MultiStack:
    def __init(self,size):
        self.numberofstack = 3
        self.fulllist = [0] * (self.numberofstack * size)
        self.listsize = [0] * self.numberofstack
        self.stacksize = size
        
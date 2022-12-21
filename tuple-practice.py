#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:03:52 2022

@author: ananyapa
"""

tup1 = (1,2,3,4)
tup2 = (2,3,4,5)
print(tup1+tup2)
print(tup1*3)


list('abcdef')
print('-'*30)

tupa = 'a','b'
tupb = ('a','b')
tupa == tupb

#tupa = ((0,1),(1,2),(2,3))
#res = sum(n for _,n in tupa)
#print(res)

tupa = ()
print(tupa.__len__()) # Throws Exception

lis = [1,2,3]
init_tuple = ('python',) * (lis.__len__() - lis[::-1][0])
print(init_tuple)

init_tuple = ('python',) * 3
print(type(init_tuple))

intuple = (1,) *3
intuple[0] = 2
print(intuple)

intuple = ((1,2),)*7
print(len(intuple[3:8]))
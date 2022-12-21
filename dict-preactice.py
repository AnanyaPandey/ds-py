#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:02:50 2022

@author: ananyapa
"""
# This is for the dictionary practice

fruit = {}
def addone(index):
    if index in fruit :
        fruit[index] += 1
    else :
        fruit[index] = 1
        
print(fruit)

mydict={}
mydict[(1,2,4)] = 8
mydict[(4,2,1)] = 10
mydict[(1,2)] = 12
sum=0
for k in mydict :
    sum += mydict[k]
print(sum)
print(mydict)


box = {}
jar = {}
crate = {}
box['biscut'] = 1 
box['cake'] = 3
jar['jam'] = 4
crate['box'] = box
crate['jar'] = jar
len(crate)

dic = {'c':97,'b':96,'a':98}

for _ in sorted(dic):
    print(dic[_])
    

rec = {'name':'python', 'age':'20'}
r = rec.copy()
print(id(r)==id(rec))

rec = {'name':'python', 'age':'20'}
id1 = id(rec)
#rec = {'name':'python', 'age':'20'}
id2 = id(rec)
id1 == id2






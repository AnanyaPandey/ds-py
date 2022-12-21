#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 22:43:41 2021

@author: ananyapa
"""

# program to 
import numpy as np
import pandas as pd

ser1 = pd.Series([1,2,3,4,5,6,7,8,10], name='trial1')

#chceking the type
type(ser1)

#converting series to list 
serlist = ser1.tolist()

# add subtract two series
ser2 = pd.Series([11,12,13,14,15,16,17,18,19])
adds = ser1+ser2
subs = ser2-ser1
divds = ser2/ser1


# Compare two series

ser1 == ser2
ser2 > ser1  # Returns a series of boolean 

# converting dict to series
dict1 = dict({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800})

sernew = pd.Series(dict1)

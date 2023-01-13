# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:49:39 2023

@author: pandey
Queue using py modules
"""
print('-'*30)
print('Collections Queue')
print('-'*30)
from collections import deque
newque = deque(maxlen=5)
print(newque)
newque.append(11)
newque.append(12)
newque.append(15)
newque.append(15)
print(newque)
print(newque.popleft())

# Queue module
print('-'*30)
print('Module Queue')
print('-'*30)
import queue as Q
newque = Q.Queue(maxsize=5)
print(newque.qsize())
newque.put(11) # enqueue
newque.put(12)
newque.put(13)
newque.put(14)
newque.put(15)
print(newque.qsize()) # size 
print(newque.full()) # isfull
print(newque.get()) # Dequeue
print(newque)

# Multiprocessing Queue module

print('-'*30)
print('Multiprocessing Queue')
print('-'*30)

from multiprocessing import Queue

newque = Queue(maxsize=3)
newque.put(1)
newque.put(2)
newque.get(1)
print(newque)








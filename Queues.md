# Queues

### Queue is a simple queue a line a linear list of any thing. queue of people queue of objects or any data structure. 

Queue is a first in first out data structure unlike stacks the person who is first will be first just like any real life queue.any person or object adding to the queue has to join at the end. addition from the end but deletion from the front.elements are served in FIFO. 

#### Applications which need FIFO need queue data structure, 

1. POS systems. In. a retail store people line up in a queue to get billed. 
2. Incoming phone call queue
3. Printer jobs queue. 

### Queues can be circular as well. 

Queue with fixed capacity can be circular which mesn that we can use the space created by the elements which got deleted or served. we do not need to create extra space for the new addition element to the queue.

1. Create a queue with fixed length space. (say 6 elements)
2. add element ( front and end both point to the same element)
3. Keep adding emenents. 
4. Once any element is dequeued ( deleted / served ) move the front to one ahead.
5. we have one empty cell. (first which got deleted)
6. **To make this queue circular update the END pointer to the latest deleted element node.**

## Queue Operations

* Create
* Enqueue
* Dequeue
* Peek ( top )
* isEmpty
* isFull
* DeleteQueue

Queue can be created with python list of linkedlist or any other data structure depending on the need of applications. 
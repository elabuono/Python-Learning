"""
A deque based on the myQueue class.
Author: Erica LaBuono
Date: 10/17/15
"""

from myQueue import *

class DequeViaQueue(struct):
    _slots = ((Queue, 'queue'))

def createDeque():
    return DequeViaQueue(EMPTY_NODE, EMPTY_NODE, 0)

def enqueue_front(element, deque):
    pass

def emptyDeque(deque):
    return deque.front == EMPTY_NODE

def dequeue_front(deque):
    pass



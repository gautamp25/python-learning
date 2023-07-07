"""
Example: Thread communication
covered- thread synchronisation,locking mechanism, and thread communication.
Queue:
    FIFO- First In First Out
    - queue.Queue() class
    - syntax-
        import queue
        my_que = queue.Queue(maxsize)
        maxsize: optional argument
    - put(item,block=True):
        This method is used to insert element into the queue.
    - get():
        This method is used to delete/get elements from queue.

    Benefits:
        - Thread safe: No race condition
        - Implements all the required locking semantics
"""
from threading import Thread
from queue import Queue
from time import sleep

def producer(my_que):
    print("Producer: Running")
    n = int(input("Enter the number of student:"))
    for i in range(n):
        marks = float(input(f"Enter the marks of student {i}:"))
        my_que.put(marks)
    my_que.put(None)
    print("Producer: End")

def consumer(my_que):
    print("Consumer: Running")
    while True:
        item = my_que.get()
        if item is None:
            break
        print(f"Got the {item}")
    print("Consumer: End")

my_que = Queue()
t1 = Thread(target=producer,args=(my_que,))
t2 = Thread(target=consumer,args=(my_que,))

t1.start()
t2.start()
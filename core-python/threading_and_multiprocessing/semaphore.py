"""
    Semaphore can be used to limit the access to the shared resources with limited capacity.
    Use BoundedSemaphore in case if acquire or release is more than one.
    Steps:
        1. Create an object of Semaphore class
            syntax- s = Semaphore()
        2. Acquire lock using acquire()
            syntax- s.acquire()
        3. Release lock using release()
            syntax- s.release()
    e.g Student exam result- 100 thread at a time.

"""

from threading import *
from time import sleep
obj = BoundedSemaphore(3)
def display(name):
    # acquire: decrement count
    obj.acquire()
    for _ in range(5):
        print("Hello\n")
        print(name)
        sleep(4)
    obj.release()
    obj.release()
    # release: increment count
  
t1 = Thread(target=display,args=("Thread-1",))
t2 = Thread(target=display,args=("Thread-2",))
t3 = Thread(target=display,args=("Thread-3",))
t4 = Thread(target=display,args=("Thread-4",))
t5 = Thread(target=display,args=("Thread-5",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
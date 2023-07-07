"""
    Race condition:
        - It is bug generated when you do multi-processing.
        - It occures because two or more threads tries to update the same variable
            and result into unreliable output.
        - Concurrent access to shared resource can lead to race condition.

    Thread synchronization Technique:
        - A common approach is to protect the critical section of code.(Prevent concurrent access)
        - We have following thread synchronization technique-
            1. Locks
            2. R-Lock
            3. Semaphore

    Locks in Python-
        - Threading module provide a Lock class to deal with the race condition
        Lock has two states:
            1. Locked- The lock has been aquired by one thread and any
                thread that makes an attempt to acquire it must wait until it is released
            2. Unlocked- The lock has not been acquired and can be acquired by the next thread
                that makes an attempt.
        
        Steps:
            1. Create an object of Lock class
                Syntax-
                    from threading import *
                    myLock = Lock()
            2. Acquire lock using acquire()
                Syntax-
                    myLock.acquire()
                    - Change the state of code to locked
                    - Other threads have to wait until lock is released by current working thread
                        syntax- lock_obj.acquire([blocking=True],timeout=-1)
            3. Release lock using release()
                Syntax-
                    myLock.release()

        Practical example in example.py file.
"""

# Bus ticketing System
from threading import Thread,current_thread

class Bus:
    def __init__(self,name,available_seats):
        self.available_seats = available_seats
        self.name = name

    def reserve(self,need_seat):
        print("Available seats are:", self.available_seats)
        if self.available_seats>=need_seat:
            nm = current_thread().name
            print(f"{need_seat} are allocated to {nm}")
            self.available_seats-=need_seat
        else:
            print("Seats are not available")

obj = Bus("VRL Travels",2)
t1 = Thread(target=obj.reserve, args=(2,), name='GTM')
t2 = Thread(target=obj.reserve, args=(1,), name='SNL')
t1.start()
t2.start()
"""
    RLocks in python
        - You cannot acquire multiple times using Lock mechanism.

        - By using RLock, you can acquire() multiple times
        - RLock is just a modified version of Lock

        Steps:
            1. Create an object of RLock class
                syntax-
                    from threading import *
                    mylock = RLock() 
            2. Acquire lock using acquire()
                syntax-
                    mylock.acquire()
            3. Release lock using release()
                syntax-
                    mylock.release()

    IMP- RLock maintain details of runing threads

    In Lock & RLock, at a time only one thread is allowed to execute.
    If requirement is to execute a particular number of threads at a time 
    then Semaphore is used.
"""

from threading import *

rlock_obj = RLock()
class Bus:
    def __init__(self,name,available_seats, rlock):
        self.available_seats = available_seats
        self.name = name
        self.rlock = rlock
    def reserve(self,need_seat):
        self.rlock.acquire()
        self.rlock.acquire()
        print(self.rlock)
        print("Available seats are:", self.available_seats)
        if self.available_seats>=need_seat:
            nm = current_thread().name
            print(f"{need_seat} are allocated to {nm}")
            self.available_seats-=need_seat
        else:
            print("Seats are not available")
        self.rlock.release()
        self.rlock.release()

obj = Bus("VRL Travels",2,rlock_obj)
t1 = Thread(target=obj.reserve, args=(2,), name='GTM')
t2 = Thread(target=obj.reserve, args=(1,), name='SNL')
t1.start()
t2.start()
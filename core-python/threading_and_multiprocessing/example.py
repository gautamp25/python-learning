from threading import *
from time import sleep


mylock = Lock()

def task(mylock,msg):
    mylock.acquire()
    for _ in range(5):
        print(msg)
    sleep(3)
    mylock.release()

t1=Thread(target=task,args=(mylock,'Hello World'))
t2=Thread(target=task,args=(mylock,'Welcome'))

t1.start()
t2.start()


lock_obj = Lock()
class Bus:
    def __init__(self,name,available_seats, lock):
        self.available_seats = available_seats
        self.name = name
        self.lock = lock
    def reserve(self,need_seat):
        self.lock.acquire()
        print("Available seats are:", self.available_seats)
        if self.available_seats>=need_seat:
            nm = current_thread().name
            print(f"{need_seat} are allocated to {nm}")
            self.available_seats-=need_seat
        else:
            print("Seats are not available")
        self.lock.release()

obj = Bus("VRL Travels",2,lock_obj)
t1 = Thread(target=obj.reserve, args=(2,), name='GTM')
t2 = Thread(target=obj.reserve, args=(1,), name='SNL')
t1.start()
t2.start()
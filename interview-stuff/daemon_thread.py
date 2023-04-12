from threading import Thread,current_thread
from time import sleep
"""
Daemon Thread- Is a thread which runs continuously in the background.
It provide support non-daemon threads 
- Default Nature of Thread
    - Main thread is always non-daemon thread.
    eg:
        mt = current_thread()
        print(mt.getName())
    - Rest of the threads inherits daemon nature from their parents.
        1. If parent thread is non-daemon then child will become non-daemon & vice versa.

    - When last non-daemon thread terminates, automatically all daemon threads
        will be terminated. We are not required to terminate daemon thread
        explicitly.

target- It represents the function on which thread will act.
args - It represents a tuple or arguments which are passed to the function.
"""
def disp():
    print("Disp function..")
    t2=Thread(target=show)
    print('T2:',t2.isDaemon())
    t2.start()

def show():
    print("Show function\n")
    

mt = current_thread()
print("Name:",mt.getName())
# print(mt.isAlive)
print("MT:",mt.isDaemon())

t1 = Thread(target=disp)
print('T1 Before:',t1.isDaemon()) # daemon-function/method
print("T1 Name: ",t1.getName())
t1.setDaemon(True)
print("T1 After:",t1.daemon) # daemon-property
t1.start()
t1.join()
print("Main Thread.!")
print("*"*30)



def teacher():
    for i in range(1,11):
        print("Teaching Session:",i)
        sleep(1)


t1 = Thread(target=teacher)
t1.setDaemon(True) # Now this is Daemon thread
t1.start()
sleep(6)
print("Exam finished !", current_thread().name)
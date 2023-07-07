"""
Types of Threads
    1. Non-Daemon thread(Non-supportive threads)- Program will not terminate until all non-daemon threads gets completed.

    2. Daemon thread(Supportive threads)- When all non daemon threads gets terminated, automatically daemon threads also
        get terminated 
        - Daemon thread is a thread which runs countinuously in background and provide support to other non-daemon threads.

    Use of Daemon thread:
        Daemon threads are often used for tasks such as monitoring, background services and cleanup operations.

    What decides threads daemon nature?
        - e.g t1 = Thread(target=task)
            t1.daemon is True then its daemon else non-daemon.
    How to change daemon nature for the thread?
        - t1.daemon = True
        Note: We cannot change daemon nature of running thread
            Default daemon nature of main thread is False.

    Daemon nature get from Parent thread. Daemon nature depends upon parent thread if parent thread is Daemon then newly created thread will be daemon.

"""
from threading import *

# obj = current_thread()
# print(obj.daemon)

def display():
    print("Display function")
    # daemon nature is depends on parent thread. here t1 is parent thread
    t2 = Thread(target=demo)
    print("Daemon nature of t2 is:",t2.daemon)

def demo():
    print("Demo function")
t1 = Thread(target=display)

print("Daemon nature of t1 is: ", t1.daemon)
t1.daemon = True
print("Daemon nature after changes is: ", t1.daemon)

t1.start()
print(main_thread())
print("This is main thread")
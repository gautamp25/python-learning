"""
    Thread Communication:
    - In concurrent programming, sometimes we need to co-ordinate threads
    - Threads communicate with each other via signals.

    Three ways:
        1. By creating event object
        2. By creating condition object
        3. By using queue module.

        1. Using Event:
            - using event object we can communicate in only two threads.
            - It maintains flag default value is False.
            Steps-
                - First we have to create an event object
                - Create two threads which will communicate 
                - Put t2 thread in waiting by using wait() method - in thread 2 code wait method must be implemented.
                - Use set() method in/after t1 threads code
                    set():-
                        - set the internal flag to True
                        - If flag is True, waiting thread is awakened
                    clear():-
                        - reset the internal flag to False
                        - other thread will wait() again.
                    is_set():-
                        - Return True if and only if internal flag is True.
                            e.g if event.is_set():
                                do something.....
                    wait([timeout]):-
                        - Calling this function keep other thread on wait until flag is set to True
                        - Block until the internal flag is true

"""

import threading
from time import sleep

e_obj = threading.Event()
def task():
    print("Game is started")
    sleep(3)
    e_obj.set()


def end():
    e_obj.wait()
    if e_obj.is_set():
        print("Game session ended")
    

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)

t1.start()
t2.start()
"""
    Exception:
    For main thread-->sys.excepthook
    For created thread-->threading.excepthook->sys.excepthook 
    WHAT HAPPENS FOR EXCEPTION IN THREAD?
        - The interpreter calls threading.excepthook() with one argument
            i.e named tuple with 4 arguments.
            1. the exception class
            2. exception instance/value
            3. a traceback object
            4. Thread name
"""

import threading
from time import sleep
# created custom hook
def custom_hook(args):
    print("Exception occured.")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

def display():
    for _ in range(5):
        sleep(0.5)
        print("hello:"+10)

def show():
    for _ in range(5):
        print("Hello")
        sleep(0.5)

threading.excepthook = custom_hook
t1 = threading.Thread(target=display)
t2 = threading.Thread(target=show)

t1.start()
t2.start()
t1.join()
t2.join()
for _ in range(5):
    print("Bye")
# Thread communication example

# 1. Traffic light signal
# 2. File handling

import threading
from time import sleep

e = threading.Event()
def signal():
    try:
        while True:
            print("Signal is Green")
            e.set()
            sleep(5)
            print("Light is Red")
            # e.clear()
            print("STOP")
            sleep(5)
            e.set()
    except KeyboardInterrupt:
        pass


def msg():
    e.wait()
    while e.is_set():
        print("You can go")
        sleep(0.5)
        e.wait()
    
    
    


t1 = threading.Thread(target=signal)
t2 = threading.Thread(target=msg)

t1.start()
t2.start()
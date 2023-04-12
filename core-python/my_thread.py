import threading
from time import sleep

e = threading.Event()


def light_switch():
    while True:
        print("light is Green")
        e.set() # flag True
        sleep(5)
        print("Light is Red")
        print("Stop..!")
        e.clear()
        sleep(5)
        e.set()
        # sleep(5)

def traffic_msg():
    e.wait()
    while e.is_set():
        print("You can go..!")
        sleep(0.5)
        e.wait()
   
    

t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=traffic_msg)
t1.start()
t2.start()
t1.join()
t2.join()
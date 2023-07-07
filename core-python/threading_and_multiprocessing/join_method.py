"""
When to use join() method?
    If a thread wants to wait for some other thread, then we should go for join() method.


"""
from threading import Thread
from time import sleep

def display():
    for _ in range(5):
        print("Welcome!")

def show():
    for _ in range(5):
        print("Let's start the program..")

t1 = Thread(target=display)
t2 = Thread(target=show)
t1.start()
# t1.join()
t2.start()
t2.join()


for _ in range(5):
    print("Hello World")


def upload():
    for _ in range(4):
        print("Video uploading started...")
        sleep(3)
        print("Video uploaded.")

def send_notification():
    print("New video uploaded.")

t3 = Thread(target=upload)
t4 = Thread(target=send_notification)

t3.start()
t3.join()
t4.start()




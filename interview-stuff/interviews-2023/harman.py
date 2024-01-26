# Multithreading

# 1. print num
# 2.check print num 1-10
from threading import Thread

nums = []
def print_num(num):
    for i in range(num):
        print(i)
        if i<=10:
            t2 = Thread(target=check_num)
            t2.start()
def check_num():
   print("Done")

t1 = Thread(target=print_num, args=(11,))
t1.start()
# t2.start()
# list and array
# decorator
# Multi-stage builds
# what is Docker
# docker image vs docker container
# dockerfile


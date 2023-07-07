# File handling

import threading
from time import sleep

e = threading.Event()


content = ""
def read_file():
    f = open("file1.txt")
    for _ in range(5):
        content += f.readline()
        print(f.readline())
        e.set()

def write_to_file():
    e.wait()
    if e.is_set():
        f2 = open("file2.txt",'w')
        f2.write(content)


t1 = threading.Thread(target=read_file)
t2 = threading.Thread(target=write_to_file)

t1.start()
t2.start()
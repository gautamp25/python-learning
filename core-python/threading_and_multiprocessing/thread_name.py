"""
Thread Names:
    1. Each thread has a name
    2. Naming:-Thread-[%d]
        First thread-Thread-1
        Second thread-Thread-2

    3. Name of the thread is stored in 'name' attribute of Thread object

    4. Main thread name- MainThread

- Thread Identifier-
    1.
    
        1. Each thread has unique identifier(id) within python process
            assigned by Python Interpreter.
        2. Read only positive integer and unique in process
        3. Assigned after starting thread.
        4. This identifier is stored in an instance variable-'ident'

    2. Native thread-
        1. Each thread has unique identifier assigned by the operating system
        2. property name- native_id(assigned after thread has started)
        3. Note-generally, ident and native_id are same

    PID- Identifier for your process(program)
    OS module-getpid()
"""
from threading import Thread,current_thread
import os
def display():
    for _ in range(4):
        print("Thread-1")

def show():
    for _ in range(4):
        print("Thread-2")

t1 = Thread(target=display)
t2 = Thread(target=show)
print(t1.name)
print(t2.name)
print(t2.getName())
print(current_thread().name)

# we can change name of the thread
t1.name="Gautam"
print(t1.name)
t2.setName("GTM")
print(t2.name)
t1.start()
t2.start()
print("Thread id",t1.ident)
print("Thread native_id-",t1.native_id)
print("Process id",os.getpid())

"""
What is Thread?
    - A thread is operating system object that executes instructions/program.

    1. A thread is a separate flow of execution in program.
    2. Thread- Represents task/ sub program

Advantages-
    - Improve performance of the system or application.
    - Reduce response time of websites or applications
    - Normal program- 1 flow
        Program with n threads- n flows

Applications-
    - Video games. e.g PUBG
    - Multi-media graphics
    - Animations

What is Main Thread?
    - Run:- Python Interpreter starts
        - Python Interpreter request OS for creating one thread
        called as Main Thread.
    - Any process have at least one default thread called as main thread
    - Main Thread is created by PVM(Interpreter) 

    
Two types of multi-tasking
    1. Process based multi-tasking
        - Each task is an independent program/process.
        - Used in OS level

    2. Thread based multi-tasking
        - Each task is an independent thread (separate part of program)
        - Used in programmatic level.

How to create Thread?
    Steps:
        1. Import Thread class from threading module
        2. Create a function containing code to be executed parallaly
        3. Create an object of Thread class
        4. Start created thread using start() method.
         
"""

# import Thread class
from threading import Thread,current_thread

# create a function containing code to be executed parallaly
def display(n):
    print("t1 thread details:",current_thread())
    for i in range(n):
        print("Learning thread")
        # print(msg)
        
# Create new thread here
t1 = Thread(target=display,args=(5,))
# start the new thread
t1.start()
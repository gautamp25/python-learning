"""
    Built-in Functions in multithreading
        1. is_alive()- check thread is running or not
        2. main_thread()- Returns main threads details
        3. active_count()- Number of running threads
        4. enumerate()- List of all running thread
        5. get_native_id()- Know native id of thread

"""

from threading import Thread,main_thread,current_thread,active_count,enumerate,get_native_id

def display():
    print("Native id of t1 thread", get_native_id())

    print(current_thread())
    print("Main thread details- ",main_thread())
    for _ in range(4):
        print("Hello World \n")

def show():
    for _ in range(4):
        print("Thread-2 \n")
t1 = Thread(target=display)
print("Before",t1.is_alive())
t1.start()
print()
print("Native id of main thread", get_native_id())
print()
print("No of active threads-",active_count())
print("After",t1.is_alive())
print("List of all active threads-",enumerate())
"""
1. Main Memory(Short term memory):
    - Primary Memory:-he temporary main memory gets deleted when the computer gets shut down. 
    - It is also refered to as Random-Access Memory (RAM)- volatile
    Main Memory Overview
        - RAM is Accessible by CPU- this RAM is stored on the motherboard of computer.
        - Data and logic loaded into the RAM for execution.
        - Fast to access
    RAM Overview
        - Logic loaded into RAM
        - Variables and objects are stored on RAM
        - RAM can get full - by creating more objects and varaibles

    RAM Management
        - Hardware
        - Operating system
        - Applications
        Memory management by Application-
            - Allocation- A piece of memory gets allocated for certain bit of information
                Two types of memory allocation
                1. Static- static allocation occurs before the program is executed.
                    - compile time,prior to the program execution

                2. Dynamic- Happen during runtime.
                    - runtime, happens during the execution of the program


            - Deallocation- when it's no longer needed.

2. Secondary Storage(Long term memory):
    - Secondary Memory:- Secondary memory is long-term memory, such as files and programs on your hard-drive.



Stack Memory-
    - Many languages work with stack and heap
    - Exact implementations differ
    - LIFO(Last-In, First-Out)
    Stack Overview-
        - Area on RAM-Stack area is part of the RAM memory
        - store variables created by your functions
        - Stack records
        - Variables created by functions are only accessible to these functions theirselves

        Call Stack-
            - Order of the functions
            - Points to the current stack record

    Stack Overflow-
        - Stack has a maximum number of records
        - Records have a maximum size
        - Stack overflow error if the limit exceeded
        - Main memory->function 1->function 2(if certain value needs to be available to diff functions & even diff.stacks at the same time, this is where
        Heap comes in.)


Heap Memory-
    - Part of RAM
    - Used for storing values that need to be accessible through more than one function/throughout the entire application.
    - e.g freezer while cooking if anything needed we can access. Lefover- will get to next accesser.

Smilarities Heap & Stack:
    - Both are areas on RAM
    - They are needed to run an application
    - Both can hold values needed for program execution

Difference Heap & Stack:

    Comparision of Memory types:
        - Heap Memory- Is used for variables,values & objects that needs to be accessible globally.
        - Stack Memory- Stack keeps order of execution and the internal values of each function, this is done in stack record.
    Deallocation:
        - Heap Memory- It can stay there for the full application run time. Heap memory can be deallocated when it doesn't have connection to stack anymore.
            1. Elements on heap are accessed via their memory address
        - Stack Memory- stack memory can be deallocated when function is finished executing.

        - Accessing stack items is faster than accessing heap items.
    Concurrency:
        - Stack record can only accessible by its owner thread.(Stack is usually considered more secure)
        - Heap can be accessible by any thread


* Allocation:
    - The assigning of memory address and reserving it to store a certain value, program, or process is called memory allocation.

    Types of memory allocation
        - Static- memory created once and persists until the program ends
        - Dynamic- all types of data are stored in the same memory.

        Dynamic memory allocation-
        This happens whenever we need to create new values on the heap.
            - Adding new values to the heap
                1. select memory area
                2. write value or reserve area
                3. Give the pointer to the memory address to a variable
* Dealocation:
    - The releasing of piece of memory and making it available again is called deallocation.
    Deallocation of Stack Memory- easy
        - When function is done, the associated stack record gets removed.

    Deallocation of Heap Memory- slightly more complicated
        - Fragmentation of the heap memory.
        



"""
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
    - e.g freezer while cooking if anything needed we can access. Leftover- will get to next accesser.

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
    Deallocation of Stack Memory- It is sort of easy
        - When function is done, the associated stack record gets removed.

    Deallocation of Heap Memory- slightly more complicated
        - Fragmentation of the heap memory.

Garbage Collection-
    - Freeing the heap memory
    - Dangling Pointer Bug can be avoided by garbage collection

    Counter-
        - Object would hold a counter
        - Counter showed number of references to the object
        - Problem with cyclic references- teo objects referencing each other
        

Sweeping Options-
    1. Normal sweeping
    2. Sweeping with compacting
    3. Sweeping with copying- copying unmarked elements to other memory region and then delete full block

    Which statement best describes the heap memory?
    Ans-It is the memory area of the RAM used for storing values that need to be accessible throughout the entire application.

    What is a similarity between the heap and the stack?
    Ans- Both are located on the RAM memory.

    Which statement best describes memory allocation?
    Ans- The assigning of a memory address for a certain value.
    Memory allocation is the assignment of a certain memory address for a certain value. 

    When can a piece of memory be deallocated?
    Ans- when it's no longer linked to the stack
    If it has no links to the stack, it's no longer needed and it can't be addressed by the stack anymore.

    What is an advantage of automatic garbage collection?
    Ans- It's less prone to errors.
    When the garbage collector takes care of it, it won't forget to deallocate when an item is ready. 

    Why does garbage collection in some implementations require stopping the execution of the application?
    Ans-Because it needs to determine which elements on the heap have a connection to the stack, and remove the ones
      from the heap that don't. If after this marking phase, the program is still executing, elements that are not marked as still needed can be added and will be removed.

    What is the main memory?
    Ans- The memory that's needed to run programs.

    What is stored on the stack memory?
    Ans-  A function's temporary variables
    This is correct. The stack contains of a record per function, containing variables that are temporarily needed to execute the function. 


    Memory in C-
        - Stack
        - Heap
        - BSS(Block Starting Symbol)- Is a special segment for a static and global variables that 
            are un-initialized at compiled time
        - DS(Data segment)- A container of global and static variables that have virtual address space in your program
            *Is for initialized global and static variables 
        - Text- compiled code that's being stored


    Functions to assign memory-
        - malloc(memory allocation): a method for dynamically allocating blocks of memory of specific sizes is used. 
        - calloc(contiguous allocation): a method for dynamically allocating blocks of memory and initializes to zero
        - realloc(reallocation): a method for dynamically reallocating blocks of memory

        malloc & calloc-used to assign a memory area on the Heap and realloc is used to reassign a new area where you 
        need to resize the memory block

        - Allocator:
            Finds a block of memory of the right size

    Three key concepts for python allocator-
        1. Arena- Arenas are largest bits of memory
            python memory consists of multiple arenas & these are kept in link list
        2. Pool- On arenas, we have pools and pools contain blocks
            Pools have state, they can either be used, full or empty.
        3. Block- Blocks are actaul memory addresses that are going to be assigned. all the blocks on pool are same size.

    Linked List:usable_arenas-
        The arenas are on a doubly linked list called usable arenas.


 Memory Leaks-
        - Accumulation of objects on the memory that are no longer needed.
        - This leads to the application or the whole system slowing down

    Deep copy-
        - Creating copies of the object and its mutable attributes and their mutable attributes, etc   


        memory_profiler  
        python -m memory_profiler filename.py  

""" 
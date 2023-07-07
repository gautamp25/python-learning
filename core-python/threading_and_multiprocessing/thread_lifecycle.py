"""
Recap:
    1. A Thread is flow of excution in a computer program 
    2. Every Python program has at least one thread of execution called the main thread.
    3. Both processes and threads are created and managed by the underlying operating system.
    4. Sometimes we may need to create additional threads in our program in order to execute code 
        concurrently.
    5. We use threading module for that
    6. sometimes we get Unreliable output because of multiple threads called as Race Condition. 


- 'Each Thread follows the same life-cycle'
    1.New Thread
    2.Running Thread<=> blocked thread
    3.Terminated Thread

Interview Questions:
    1. Difference between creating and starting a thread?
        Ans- When we create new thread(Thread.new) then it not starts quickly, we need to start it by using start() method.
    Period between creation to start is called stage-1 i.e New Thread 
    2. Differnce between run and start?
        Ans- When we call start() method then thread goes into running state(i.e runnable).
        If there is any exception raise then thread terminates with exception message else it terminate normally.
    3. Difference between blocked and terminated?
        Ans:- Sometime thread goes into sleeping state called blocked state bcoz thread needs to wait for IO.
            durring thread communication thread go into sleeping state.
            When thread execute completely it terminate normally.(Thread.exit)



    
"""

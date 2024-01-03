
"""
Estuate Interview Full Stack (11-12-2023 11:00 AM -11:45 AM Google Meet):
Questions Asked-
    1. Diff. in map and lambda function?
    2. why we call lambda as annonymous function?
    3. map function, filter function?
    4. What is Decorators, Generator, Iterator?
    5. How memory is managed in python?
    6. Diff in .py and .pyc?
    7. Namespaces in python?
    8. count element in list without built in function using list comprehension, get odd numbers from list- Coding Q
    9. List comprehension in python. get odd and even numbers using list comprehension.
    10. How we use database in flask or Django?
    11. How to delete file in os, cmd? os.remove()
    12. Web development work?
"""

lst = [1,2,3,4]
# # using for loop
cnt=0
for i in lst:
    if i!= None:
        cnt+=1
print(cnt)

# # Using list comprehension
my_list = [1, 2, 3, 4, 5]

list_length = sum([1 for _ in my_list])
print(list_length)

# List Comprehension
"""
1. List comprehension is a concise way to create and manipulate lists in Python.
2. It allows you to generate a new list by iterating over an existing iterable (such as a list, tuple, or string) and applying transformations
    or conditions to each element.
3. List comprehensions are characterized by their compact syntax and are often used as a more readable alternative to traditional for loops.
"""

# The basic syntax of a list comprehension is as follows:
new_list = [expression for item in iterable if condition]

# Here's a breakdown of each component:
#     expression: The transformation or operation to be performed on each item.
#     item: The variable representing each element in the iterable.
#     iterable: The existing collection or sequence of elements to iterate over.
#     condition (optional): A conditional statement that filters which items are included in the new list.


# Here's an example to demonstrate the use of list comprehension:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_numbers)

"""
In the above code, a new list squared_numbers is created using list comprehension. 
It squares each even number from the numbers list, filtering them using the condition x % 2 == 0.
The result is [4, 16] since only 2 and 4 satisfy the condition.

USE:
List comprehensions are powerful and flexible, allowing you to perform various operations on iterables in a concise and readable manner.
They are commonly used for tasks like filtering, mapping, and transforming data within lists.

"""

# What is lambda function?
"""
    A lambda function is a small anonymous function in Python that can take any number of arguments but can only have one expression. 
    It is defined using the lambda keyword, followed by the arguments and a colon, and then the expression.

    Here's an example of a lambda function that adds two numbers:

    add = lambda x, y: x + y

    In this example, the lambda function takes two arguments, x and y, and returns their sum.

    Lambda functions are often used in conjunction with other built-in functions like map(), filter(), and reduce().
    They provide a concise way to define simple functions without the need for a separate def statement.
    For example, with map(), you can use a lambda function to apply a transformation to each element of a list:

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, numbers))

    In this example, the lambda function is used to calculate the square of each number in the numbers list. The map() function then applies this lambda function to each 
    element of the list, returning a new list with the squared numbers.
    
    Use:
        Lambda functions are also useful in situations where you need to pass a simple function as an argument to another function, such as in sorting or filtering operations.

    Overall, lambda functions provide a convenient way to define small, one-time use functions without the need for a formal function definition.
"""

# Why it is called Anonymous function?
"""
    An anonymous function in Python is a function that is defined without a name. 
    It is also known as a lambda function. 
    It is typically used when we need a simple function that is only used once and does not require a formal definition.
    Lambda functions are often used as arguments to higher-order functions or in situations where a named function would be unnecessary or cumbersome.

    They are defined using the lambda keyword, followed by the parameters and a colon, and then the expression to be evaluated. 
    For example, a simple lambda function that adds two numbers can be defined as follows: add = lambda x, y: x + y.
"""

# Explain map() function?
"""
    The map function in Python is a built-in function that applies a given function to each item in an iterable (such as a list or a tuple) and 
    returns a new iterator with the results. 
    It takes in two arguments: the function to apply and the iterable to apply it to.

    Syntax:
    map(function, iterable)

    Here, function is the function to be applied to each item in the iterable,
    and iterable is the iterable object (e.g., a list) on which the function is to be applied.

    e.g
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(squared_numbers)

    In this example, the map function is used to apply the lambda function (which squares a number) to each element in the "numbers" list.
    The result is a new list, "squared_numbers", which contains the squared values of the original numbers.

    USE:
    We use the map function when we want to apply the same operation to every item in an iterable and collect the results.
    This can be useful when we need to perform a calculation or transformation on each element of a list or tuple.

"""

# Explain filter() function?
"""
    The filter() function in Python is a built-in function that allows you to filter out elements from a sequence based on a given condition.
    It takes two arguments: a function and an iterable. 
    The function is applied to each element in the iterable, and only the elements for which the function returns True are included in the output.

    Here's an example to illustrate how the filter() function works:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def is_even(num):
        return num % 2 == 0

    even_numbers = list(filter(is_even, numbers))
    print(even_numbers)  # Output: [2, 4, 6, 8, 10]


    In this example, the is_even() function checks if a number is even by using the modulo operator % to check if the remainder of the division by 2 is 0.
    The filter() function applies this function to each element in the numbers list and only keeps the elements for which is_even() returns True.
    Finally, the filtered elements are converted to a list and stored in the even_numbers variable, which is then printed.
"""

# Difference in map() and filter() function?
"""
    map() applies a function to each item in an iterable and returns an iterator with the results,
    while filter() returns an iterator with only the elements that satisfy a given condition.
"""

# Difference in map() and lambda function

"""
    In Python, the map() function and lambda function are both used for performing operations on a collection of data.

    The map() function takes in a function and an iterable as arguments.
    It applies the function to each element in the iterable and returns an iterator with the results. For example, if you have a list of numbers and want to square each number, you can use the map() function 
    along with a lambda function like this:

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(lambda x: x**2, numbers)


    The result will be an iterator with the squared numbers: [1, 4, 9, 16, 25].

    On the other hand, a lambda function is an anonymous function that can be defined in a single line. It is often used when you need a simple function for a short period of time, without the need to define
    a named function. The lambda function takes in arguments and returns a value based on the expression defined.

    Using the previous example, you can rewrite the map() function using a lambda function like this:

    ini

    squared_numbers = map(lambda x: x**2, numbers)
"""

# Explain reduce() function.
"""
    The reduce function in Python is a function from the functools module that is used to apply a specific function to the elements of an "iterable in a cumulative way". 
    It takes two arguments: the function to be applied and the iterable. The function is applied to the first two elements of the iterable, then to the result and the next element,
    and so on until the iterable is exhausted. The final result is returned. 
    
    Here's an example:
    from functools import reduce

    numbers = [1, 2, 3, 4, 5]

    sum_of_numbers = reduce(lambda x, y: x + y, numbers)
    print(sum_of_numbers)  # Output: 15

    product_of_numbers = reduce(lambda x, y: x * y, numbers)
    print(product_of_numbers)  # Output: 120


    In the first example, the reduce function is used to calculate the sum of the numbers in the list. 
    In the second example, it is used to calculate the product of the numbers.
"""

# What is Generator function?

"""
    A generator in Python is a special type of function that can be used to create 'iterators'.
    It allows you to define a function that returns a sequence of values, but instead of returning the entire sequence at once, it yields one value at a time. 
    This can be useful when working with large datasets or when you don't want to store all the values in memory at once.

    Generators are defined using the yield keyword instead of return.
    When a generator function is called, it returns a generator object that can be iterated over using a for loop or by calling the next() function.
    Each time a value is yielded, the generator function is paused, and the value is returned.
    The next time the generator is iterated over, the function resumes from where it left off.

    Example:
        def fibonacci_generator(n):
            a, b = 0, 1
            while a<n :
                yield a
                a, b = b, a + b

        fib = fibonacci_generator(3)
        # for i in fib:
        #     print(i)
        
        print(next(fib))  # Output: 0
        print(next(fib))  # Output: 1
        print(next(fib))  # Output: 1
        print(next(fib))  # Output:2 

        Generator objects are exhausted after the use.

        Generators can save you memory, making it easier to work with large data sets and other cumbersome tasks.
        It is memory efficient.
        slower than list.

        import sys
        some_word = ['voice','bark','apple',"convention",'crusade','perinnial']
        def gen_contains_i(words):
            for word in words:
                if 'i' in word:
                    yield word
        print(list(gen_contains_i(some_word)))
        print(id(list(gen_contains_i(some_word))))
        print(sys.getsizeof(list(gen_contains_i(some_word))))
"""
# what is iterator?
"""
    An iterator in Python is an object that can be iterated over, meaning that it can be used in a for loop or other iterable contexts.
    It must implement the __iter__() and __next__() methods.
    The __iter__() method returns the iterator object itself, while the __next__() method returns the next value from the iterator.
    When there are no more items to return, the __next__() method should raise the StopIteration 

    In Python, an iterator is an object that can be iterated or looped over. It allows you to access the elements of a container (like a list or a tuple) one by one. 
    To create an iterator in Python, you need to implement the __iter__() and __next__() methods in a class.

    Here's an example of an iterator class in Python:

    python

    class MyIterator:
        def __init__(self, data):
            self.data = data
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index >= len(self.data):
                raise StopIteration
            value = self.data[self.index]
            self.index += 1
            return value

    # Using the iterator
    my_list = [1, 2, 3, 4, 5]
    my_iterator = MyIterator(my_list)

    for item in my_iterator:
        print(item)


    In this example, the MyIterator class takes a list data as input. It has an index attribute to keep track of the current position in the list. The __iter__() method returns the iterator object itself. The __next__() method returns the next element in the list and updates the index.

    By using the for loop with the iterator object, you can iterate over the elements of the list one by one and print them.
"""

# Dict comprehension
"""
    A dictionary comprehension in Python is a concise way to create a new dictionary by specifying both the key and value expressions. 
    It follows a similar syntax to list comprehensions but uses curly braces instead of square brackets. Here's an example:

    Syntax:
    {key_expression: value_expression for item in iterable}

    Here, key_expression is the expression that defines the key for each item in the iterable, and value_expression is the expression that defines the value for each item.
    The item represents each element in the iterable, such as a list or a range.

    numbers = [1, 2, 3, 4, 5]
    squared_dict = {num: num**2 for num in numbers}
    print(squared_dict)


    This will output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.
"""
# Difference between .py and .pyc file.
"""
    In Python, the .py file is the source code file that contains the actual Python code written by the programmer. 
    On the other hand, the .pyc file is the compiled bytecode file that is generated by the Python interpreter after it compiles the .py file.
    The .pyc file is created to improve the performance of subsequent executions of the Python program. 
    When a .py file is executed for the first time, the Python interpreter compiles it into bytecode and saves the bytecode in a .pyc file. 
    The next time the program is executed, the Python interpreter can directly load and execute the bytecode from the .pyc file, which is faster than recompiling the .py file every time.
    The .pyc file is platform-independent and can be executed on any platform as long as the Python interpreter is compatible.
"""

# Memory Management
"""
    In Python, memory management is handled automatically through a mechanism called garbage collection. Python uses a technique called reference counting to keep track of objects in memory. 
    Each object has a reference count, which is incremented when a reference to the object is created,
    and decremented when a reference is deleted or goes out of scope. When an object's reference count reaches zero, it is considered garbage and can be safely deallocated from memory.

    Python also uses a garbage collector that periodically runs to detect and deallocate objects with circular references.
    Circular references occur when two or more objects reference each other, forming a cycle that prevents them from being garbage collected.
    The garbage collector identifies these cycles and frees up the memory occupied by the objects.

    Overall, Python's memory management system allows developers to focus on writing code without having to explicitly allocate and deallocate memory.
    However, it's still important to be mindful of memory usage and avoid unnecessary object creation to ensure optimal performance.
"""

# Namespace in python.
"""
    In Python, a namespace is a container that holds a set of names (identifiers) and their corresponding objects (values).
    It serves as a mapping between names and objects, allowing you to organize and manage the "names" used in your Python program.
    Namespaces play a crucial role in avoiding naming conflicts and providing a way to organize code.

    There are several types of namespaces in Python:
    1.Local Namespace:
        The local namespace is associated with a particular function or method. 
        It contains the names defined within that function or method.
        This namespace is created when the function is called and destroyed when the function exits.

        Example:
        def my_function():
            local_variable = 42
            print(local_variable)

        my_function()


    2. Global Namespace:

        The global namespace encompasses the entire module.
        It includes names defined at the top level of a script or module.
        This namespace is created when the module is imported or executed and persists until the program terminates.

        Example:
        global_variable = 10

        def print_global_variable():
            print(global_variable)

        print_global_variable()


    3. Built-in-namespace:
        The built-in namespace contains names that are part of the Python language itself.
        These names are always available and include functions like print(), data types like int and list, and other built-in functionalities.

        print(len([1, 2, 3]))  # 'len' is a built-in function

    Namespaces are organized hierarchically in Python, forming a chain of scopes. When you reference a name, Python searches for it in the local namespace first,
    then in the enclosing (if any) functions' namespaces, followed by the global namespace, and finally in the built-in namespace.

    Understanding namespaces is crucial for avoiding naming conflicts, managing variable scope, and gaining insights into how Python resolves names during execution.
    It is also fundamental for concepts like variable scope, closures, and decorators.


"""
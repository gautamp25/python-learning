"""
Table: List | Tuple

1. List is group of comma separated values within square brackets and 
square brackets are mandatory.
e.g: l=[1,2,3,4]

1. Tuple is group of comma separated values within parenthesis and
 parenthesis are optional.
e.g: t= (1,2,3,4)
    t = 1,2,3,4

2. List objects are mutable. ie once we create list object, 
we can change it's content.
eg: l[2] = 6

2. Tuple objects are immutable. ie once we create tuple object, 
we are not allowed to change it's content.
eg: t[2] = 6 # TypeError: 'tuple' object does not support item assignment

3. List objects require more memory
3. Tuple objects require less memory. if content is fixed size then tuple is choice
e.g:
    l1 = [1,2,3,4,5,6,7,8,9,10]
    l2 = [1,2,3,4,5,6,7,8,9,10]
    t1 = (1,2,3,4,5,6,7,8,9,10)
    t2 = (1,2,3,4,5,6,7,8,9,10)

4. List objects won't be reusable
4. Tuple objects are reusable

5. Performance of List is Low, ie. operations on List object require more time
5. Performance of Tuple is High, ie. operations on Tuple object require less time

6. Comprehension concept is applicable for List
6. Comprehension concept is not applicable for Tuple

IMP POINTS:
    1. In the case of Set & Dictionary objects are stored in HashCode.
    2. Lists are unhashable  .eg. s = {10,20,30,[1,2]} # TypeError: unhashable type: 'list'

7. List objects are unhashable type and hence we cannot store in Set & in Dict as keys
eg: s = {10,20,30,[1,2]} # TypeError: unhashable type: 'list'
    d = {[1,2]:'List'} # TypeError: unhashable type: 'list'
7. Tuple objects are hashable type and hence we can store in Set & in Dict as keys
eg: s = {10,20,30,(1,2)} 
    d = {(1,2):'List'}


8. If content is not fixed and keep on changing then it is recommended to go for
List objects.
eg: To store YT comment
8. If content is fixed and never changes then it is recommended to go for
Tuple objects.
eg: Allowed input values for ATM machine

9. Unpacking is possible in List but packing is not possible
eg: l = [1,2,3,4]
    a,b,c,d = l # valid
    a= 10
    b=20
    c=30
    l=a,b,c # invalide

9. Both packing and unpacking is possible in Tuple

"""
import sys
l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [1,2,3,4,5,6,7,8,9,10]
t1 = (1,2,3,4,5,6,7,8,9,10)
t2 = (1,2,3,4,5,6,7,8,9,10)
print(id(l1))
print("Size of L1:",sys.getsizeof(l1))
print(id(l2))
print("Size of L2:",sys.getsizeof(l2))
print(id(t1))
print("Size of T1:",sys.getsizeof(t1))
print(id(t2))
print("Size of T2:",sys.getsizeof(t2))


s = {10,20,30,[1,2]}
print(s) # TypeError: unhashable type: 'list'
d = {[1,2]:'List'}
print(d) # TypeError: unhashable type: 'list'

s = {10,20,30,(1,2)}
print(s) # valid
d = {(1,2):'List'}
print(d) # valid


# packing unpacking
l = [1,2,3,4]
a,b,c,d = l # valid
print(a,b,c,d)
a= 10
b=20
c=30
l=a,b,c # tuple
print(l)

"""
In Python, a List object is a dynamic array that can resize itself during runtime to accommodate a varying number of elements. While lists offer flexibility and ease of use, they may consume more memory compared to other data structures under certain circumstances. Here are a few reasons why List objects might use more memory:

    Dynamic Resizing:
        Lists in Python are dynamic arrays, which means they can grow or shrink in size as elements are added or removed. This dynamic resizing mechanism might lead to extra memory consumption, as the list may allocate more space than is immediately required to reduce the frequency of resizing operations.

    Overallocation:
        Lists in Python often allocate more space than the current number of elements to avoid frequent resizing. This overallocation is a strategy to improve performance by reducing the number of times the list needs to be resized. However, it can result in temporarily unused memory.

    Reference Counting:
        Python uses a reference counting mechanism for memory management. Each object, including elements in a list, has a reference count. Lists may have additional memory overhead to manage references and track the count of references for each element.

    Homogeneous Data Type:
        Lists in Python can store elements of different data types, and this flexibility comes with a cost. Extra memory might be required to store information about the type of each element within the list.

    Memory Fragmentation:
        Over time, as elements are added and removed from a list, memory fragmentation may occur. This fragmentation can lead to inefficient memory usage and contribute to increased memory consumption.

It's important to note that while Lists have these characteristics, they also offer valuable features such as constant-time access to elements by index, dynamic resizing, and versatility. If memory efficiency is a critical concern, and the data structure can be more rigid, other specialized data structures like NumPy arrays or Python's array module may be considered.

In summary, the memory consumption of List objects in Python can be influenced by dynamic resizing, overallocation, reference counting, support for heterogeneous data types, and memory fragmentation. Depending on the use case, other data structures with different memory characteristics may be more suitable.
"""
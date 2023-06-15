import sys

"""
    Elements of a list are stored as pointers to the elements
    rather than the values of the elements themselves.

    "The exact size of an empty list can vary across different Python versions and implementations."

    A single pointer to an element requires 8 bytes of space in a list.
    Whenever additional elements are added to the list, Python dynamically
    allocates extra memory to accommodate future elements without resizing the container.
    This implies, adding a single element to an empty list will incite Python to allocate more memory than 8 bytes.
"""
l = []
print(sys.getsizeof(l)) # 56

# Python over-allocated 32 extra bytes to accommodate future incoming elements.
l.append(0)
print(sys.getsizeof(l)) # 56+32 = 88

l.append(1)
print(sys.getsizeof(l)) # 88
l.append(2)
print(sys.getsizeof(l)) # 88

l.append(3)
print(sys.getsizeof(l)) # 88

l.append(4)
print(sys.getsizeof(l)) # 88+32 = 120
l.append(5)
print(sys.getsizeof(l))
l.append(6)
print(sys.getsizeof(l))
l.append(7)
print(sys.getsizeof(l))

l.append(8)
print(sys.getsizeof(l))

import timeit
def tm():
    d = []
    for i in range(100):
        d.append(i)

print(timeit.timeit(stmt=tm))
print(timeit.timeit("tm()",setup="from __main__ import tm"))

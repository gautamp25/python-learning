import sys
import cProfile
"""

A pipeline uses more than one generator to interact with information in combination with each other.
List Comprehensions vs Generator Expressions
    - Comprehension can be faster than generator expressions
    - Generator expressions save memory

"""
# Memory
double_lc = [n*2 for n in range(1,5000)]
double_ge = (n*2 for n in range(1,5000))

# print(sys.getsizeof(double_lc))
# print(sys.getsizeof(double_ge))

# Speed
print(cProfile.run("max([n*2 for n in range(1,50000)])"))
print(cProfile.run("max((n*2 for n in range(1,50000)))"))
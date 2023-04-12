fibonacci_cache ={}

def fibonacci(n):
    # check if n in cache retun it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n==1:
        value = 1
    elif n==2:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    # cache the value and return it
    fibonacci_cache[n] = value
    return value

for i in range(1,50):
    print(i,":",fibonacci(i))


def fib1(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

for n in range(11):
    print(n, ":", fib1(n))

from functools import lru_cache
# Least Recently Used  Cache
# default size is 128
@lru_cache(maxsize = 1000)
def fib2(n):
    if type(n) != int:
        raise TypeError("n must be positive integer")

    if n < 1:
        raise ValueError("n must be positive int")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)
    
# fib2(50)

for i in range(1,501):
    print(i, ":", fib2(i))

    
"""
How kubernetes run on locally
What is kubernetes?
"""

def multipliers(x):
  return [lambda x : i * x for i in range(4)]
bb=multipliers(2)
# for a in bb:
#   print(a.next())
print(list(bb))
# print ([m(2) for m in multipliers()])


class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x) # 1,1,1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x) # 1,2,1
Parent.x = 3
print (Parent.x, Child1.x, Child2.x) # 3,3,3

list = ['G', 'A', 'U', 'T','A','M']
print(list[6:]) # []
print (list[-6:]) # ['G', 'A', 'U', 'T','A','M']
print (list[-7:]) # ['G', 'A', 'U', 'T','A','M']



def multipliers():
  return [lambda x : i * x for i in range(4)]
    
print ([m(2) for m in multipliers()]) #[6,6,6,6]

"""The provided code demonstrates the concept of closures and the behavior of lambda functions within a list comprehension. Let's break it down step by step:


def multipliers():
    return [lambda x: i * x for i in range(4)]


Here, the multipliers function returns a list of lambda functions.
Each lambda function takes an argument x and multiplies it by i. 
The range used is range(4), which generates values from 0 to 3. 
However, the interesting part is that the lambda functions hold a reference to the variable i rather than its value at the time of creation.

print([m(2) for m in multipliers()])


In this line, a list comprehension is used to iterate over the list of lambda functions returned by the multipliers function. Each lambda function is then called with the argument 2.
The expected output would be [6, 6, 6, 6].

The unexpected result occurs because the lambda functions all refer to the same variable i. By the time the lambda functions are executed, the loop in range(4) has already completed, and the value of i is set to
its final value, which is 3. Therefore, when each lambda function is called, it multiplies 3 by 2, resulting in 6.

To achieve the desired behavior of multiplying each lambda function by a different value of i, you can use a technique called "capturing the value of i" by passing it as a default argument to the lambda function.
 Here's an updated version of the code that demonstrates this:

python

def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]

print([m(2) for m in multipliers()])


With this modification, the lambda function captures the value of i at each iteration, resulting in the expected output: [0, 2, 4, 6].
"""
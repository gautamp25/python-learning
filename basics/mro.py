# Method Resolution Order

from types import ClassMethodDescriptorType


"""python support multiple inheritance. MRO is concept used in inheritance.
 It is order in which method is searched for in classes  hierarchy.
 In python MRO is from bottom to top and left to right. Means first method is serached in class of the object,
 if it's not found then searched in immediate super class. In case of multiple super classes it is searched left to right

"""
#  Single inheritance MRO => B -> A
class A:
    def method(self):
        print("A.method() is called.")

class B(A):
    def method(self):
        print("B.method() is called.")

obj=B()
obj.method()
# O/P B.method() is called.

# example 2 MRO => C -> B -> A
class A:
  def method(self):
    print("A.method() is called")

class B:
  pass

class C(B, A):
  pass

c = C()
c.method()
# O/P A.method() is called

# example 3 - Multiple inheritance- MRO => D -> C -> A -> B

class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()
# O/P A.method() called

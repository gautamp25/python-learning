"""
    Deriving new class from existing class so that new class can inherits all members(attributes+methods)
    of existing class is called Inheritance.
    - Child class can access properties of itself plus the properties of parent class
    - Parent can't access properties of Child class

    Old clas- Parent class,Base class,Supper class

    New class- Child class, Sub class, Derived class

    Object class-
        All classes in python are derived from built in 'object' class


    - Need of Inheritance-
        - For code re-usability
        - When you have relations among classes

    How constructor works in inheritance?
        - By default, constructor of parent class available to child class.

        Constructor over-riding: 
            - If we have Parent and Child class then Child class constructor priority will be high than Parent class

"""

class Parent(object):
    # attributes+methods
    pass

class Child(Parent):
    # attributes+methods
    pass

# default object present 
# Parent class
class Employee:
    # class variable
    bonus = 2000

    #instance method
    def display(self):
        print("This is employee class method")

# Child class
class Manager(Employee):
    bonus_1 = 5000
    def show(self):
        print("This is manager class method")


m1 = Manager()
e1 = Employee()

m1.show()
e1.display()
print(m1.bonus)


# constructor example
class Father:
    def __init__(self):
        print("Father class constructor called")
        self.vehicle = "House"

class Son(Father):
    # pass
    def __init__(self):
        print("Son class constructor called")
        self.vehicle = "2 BHLK"

s1= Son()
# if no constructor in child class
# print(s1.__dict__) # {'vehicle': 'House'}

# If constructor present in child then no parent constuctor called. Constructor over-riding: 
print(s1.__dict__) # {'vehicle': '2 BHLK'}


"""
super() function-
    - using super() function, we can access parent class properties and methods.
    - This function returns temporary object which contains reference to parent class
    - It makes inheritance more manageable & extensible.
"""

class Computer:
    def __init__(self):
        self.ram = '8GB'
        self.storage = '512GB'
        print("Computer constructor called")

    def display(self):
        print("Hello World")


class Mobile(Computer):
    def __init__(self):
        super().__init__()
        # super().display()
        self.model = 'iPhone X'
        print("Mobile constructor called")

apple = Mobile()
print(apple.__dict__) #{'ram': '8GB', 'storage': '512GB', 'model': 'iPhone X'}

"""
Types of Inheritance-
    - Single inheritance:
        One Parent and one Child.
        (Object-->Parent-->Child)

    - Multi-level Inheritance:
        Parent class & Child class further inherited into new class forming 
        multiple level.
        (Object-->Parent-->Child-->Grand_Child)
    
"""

class Human_being(object):
    def __init__(self):
        print("Human being constructor called")
        self.name = input("Enter your name:")

class Employee(Human_being):
    def __init__(self):
        print("Employee constructor called")
        self.salary = input("Enter your salary:")

class Manager(Employee):
    pass
    # def __init__(self):
    #     print("Manager constructor called")
    #     self.bonus = input("Enter your bonus:")


m_obj = Manager()


"""
Hierarchical inheritance-
    - One Parent and multiple child classes
    (object-->Parent-->Child1-->Child2)
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Person display method")

class Employee(Person):
    def __init__(self,sal,name,age):
        super().__init__(name,age)
        self.sal = sal
    
    def display1(self):
        print("Employee display method")

class Student(Person):
    def __init__(self,marks,name,age):
        super().__init__(name,age)
        self.marks = marks

    def display2(self):
        print("Student display method")


s1 = Student(90,'Gtm',25)
print(s1.__dict__)

e1 = Employee(30000,'Mahesh',26)
e1.display1() # Employee display method
e1.display2() # AttributeError


"""
    Multiple Inheritance-
        - Class is derived from multiple base classes
        - Object-->Parent1-->Parent2<-->Child

        - In multiple inheritance when we add super() condition in one of the parent class
        then super method control goes to another parent class, for example Country is not Parent of State class.
        It is present in District class after State.
"""

class Country:
    def __init__(self) -> None:
        print("Country constructor called")
        self.office = "Kolkata"

class State:
    def __init__(self) -> None:
        super().__init__() #
        print("State constructor called")
        self.office = "Mumbai"

class District(State,Country):
    def __init__(self) -> None:
        super().__init__()
        print("District constructor called")
        self.office = "Pune"
    

d = District()
# Country constructor called
# State constructor called
# District constructor called
print(d.__dict__)


"""
 MRO - Method Resolution Order
    - MRO represents how properties(attributes+methods) are searched in inheritance.
    1. Python first serach in Child class and then goes to Parent class.
    Priority is to Child class.
    2. MRO follows 'Depth First Left to Right approach'

    class O:
        pass #Object
    class A:
        pass #(A,O)
    class B:
        pass #(B,O)
    class C:
        pass #(C,O)
    class X(A,B,C):
        pass #(X,A,B,C,O)
    class Y(B,C):
        pass #(Y,B,C,O)
    class P(X,Y)
        pass #(P,X,A,Y,B,C,O)
        
    3. You can use mro() method for knowing mro of any class object.
    

    Hybrid Inheritance:
        - It contains multiple type of inheritance.
        - Object-->Parent1-->Parent2<-->Child-->Child1-->Child2
"""

class A:
    pass #(A,O)
class B:
    pass #(B,O)
class C:
    pass #(C,O)
class X(A,B,C):
    pass #(X,A,B,C,O)
class Y(B,C):
    pass #(Y,B,C,O) 
class P(X,Y):
    pass #(P,X,Y,A,B,C,O)

print(P.mro()) # P -> X -> A -> Y -> B -> C -> object
print(Y.mro())


# MRO => D -> C -> A -> B-> O
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
print(D.mro())




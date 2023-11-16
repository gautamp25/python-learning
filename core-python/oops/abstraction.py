"""
In Python, an abstract class is a class that cannot be instantiated directly 
    and is meant to be subclassed by other classes.
    -Abstract classes are useful when you want to create a blueprint for a group of classes
     that share certain characteristics or behavior.

    To create an abstract class in Python, you need to use the abc module,
    which stands for Abstract Base Classes.
    This module provides the ABC class and the abstractmethod decorator, which you can use to define abstract methods.

Abstraction-
    The process by which data and functions are defined in such a way that
    only essential details can be seen and unneccessary implementations are hidden
    is called Data Abstraction.

    - Hiding complex implementation details and showing only signatures to users.

    
How Abstractions achieved in python?
    1. By using abc module- ABC class abstractmethod.
    2. Inherit your class from ABC class.
    3. Create abstract methods in your abstract class

Abstract methods- method that has a declaration but does not have an implementation.
Concrete methods- Normal methods

Abstract class- A class which contains one or more abstract methods and concrete methods.
Abstract class must have at least one abstract method.

Abstract class can be considered as Blueprint for other classes.

A class which is inhereted from ABC class 

IMP keep in mind-
    1. We can't instantiate abstract classes
    2. Abstract class require atleast one method abstract
    3. All abstract method present in abstract class must be implemented in child classes.
    Else, child class becomes abstract.
    4. If there is abstract method in class, that class must be abstract class.
    Can't instantiate abstract class Car with abstract methods 


Uses of Abstraction-
    1. When we have large code and functionalities.
    2. Your abstract class is like an API for other subclasses.
    3. Used when a third party is going to provide implementations.
    4. When we have different implementations for different objects for same component.
    5. For creating interfaces. e.g CMD prompt
        Interface in python is an Abstract class which contains only abstract methods, no concrete methods.

"""
# Syntax
from abc import ABC, abstractmethod
class Employee(ABC):
    pass
    #abstract methods
    #concrete methods

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    def color(self):
        print("The color is Red")

class MarutiSuzuki(Car):
    def mileage(self):
        print("Mileage is 30 Kmph")

class Tata(Car):
    def mileage(self):
        print("Mileage is 32 Kmph")

# car_obj = Car()
# print(car_obj) # Can't instantiate abstract class Car with abstract methods 
ms_obj = MarutiSuzuki()
ta_obj = Tata()
print(ms_obj.mileage())
print(ta_obj.mileage())
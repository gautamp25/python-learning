"""
    In Python, an abstract class is a class that cannot be instantiated directly 
    and is meant to be subclassed by other classes.
    -Abstract classes are useful when you want to create a blueprint for a group of classes
     that share certain characteristics or behavior.

    To create an abstract class in Python, you need to use the abc module,
    which stands for Abstract Base Classes.
    This module provides the ABC class and the abstractmethod decorator, which you can use to define abstract methods.

    Here is an example of an abstract class in Python:


    In this example, the Animal class is an abstract class that defines an abstract method called make_sound().
    The Dog and Cat classes are subclasses of Animal and implement the make_sound() method in their own way.

    Note that you cannot create an instance of the Animal class directly, 
    as it is an abstract class.
    You need to create an instance of a subclass, such as Dog or Cat, which implements the abstract method.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog_obj = Dog()
dog_obj.make_sound()

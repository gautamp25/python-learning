"""
CLASS- 
Class creates a user-defined data structure, which holds its own data members and member functions,
which can be accessed and used by creating an instance of that class.
Definition:- A class is like a blueprint for an object.
Points-
Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

OBJECT-
An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class
with actual values

* An object consists of :
State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.

Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
self:It's a reference to the instance of class
"""

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, My name is {self.name}")


obj = Person("Gautam")
obj.greet()


class Dog:
    # class variable
    animal = "Dog"
    def __init__(self, breed):
        # instance variables
        self.breed = breed
        
    # Adds an instance variable
    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


obj1 = Dog("Pug")
obj1.set_color("Brown")
print(obj1.get_color())

"""
 Encapsulation-
    
    What is encapsulation?
        Wrapping up data and methods working on data together in single unit(i.e class) is called 
        as Encapsulation.
        e.g class with Method & Variables.

        #Data hiding

    Access Modifiers in python:
        - Generally, we restrict data access outside the class in encapsulation.
        - Encapsulation can be achieved by declaring the data members and methods of class as private.

        Three access specifier: public, private, protected
        1. Public member- Accessible anywhere by using object reference.
        2. Private member(__)- Accessible within the class. accessible via methods only. double underscore to make private.
        3. Protected member(_)- Accessible within class and it's subclasses. single underscore to make it protected

    Advantages-
        1. Security
        2. Prevents accidental modification
        3. Simplicity
"""

class Finance:
    def __init__(self):
        self.__revenue = 100000
        self._number_of_sales = 112
    
    def display(self):
        print("Private revenue value is :",self.__revenue)


f1 = Finance()
print(f1.__dict__)
f1.display()
f1._Finance__revenue = 23
# name mangling _classname__variablename
print(f1._Finance__revenue)

class HR:
    def __init__(self):
        self.number_of_emp = 32
        f1.__revenue = 0
        print(f1.__revenue)

h1 = HR()
print(f1.__dict__)

"""
    What is oop?
        Ans- Object Oriented Pragramming is programing paradigms.programming paradigms are
        the ways of organizing programs
        * python support multiple paradigms.These are as followas
        1. Procedural oriented paradigm-arrange program in procedure,line by line like 1st instruction,2nd, 3rd and so on..
            # Problem is reusability
        2. Functional oriented paradigm-Divide program into number of function and call whenever required. focus on logic
            # Re-usability is achieved but can not solve real world problem with this
        3. Object-oriented paradigm- With oop we can solve real world problems

        - OOP is an approach of writing programs by creating classes ans objects.
        - More focus on data rather than logic
        Why OOP?
            To solve real-world problems effectively.
            OOP provides some features:
                1. Inheritance- Reusability
                2. Encapsulation-Data security
                3. Abstraction- Data hiding
                4. Polymorphism- Many forms

        What is Class?
            Ans- Clas is template/blueprint/prototype for creating objects.
            -Every object belong to some/certain class
            -Email class- email1+email2+email3
            -Class is collection of attributes and methods
            -class is a collection of objects
            -class is a user-defined datatype. eg x=100, print(type(x)), # O/P- <Class 'int'>
            - Built-in class and user-defined class

            class Email:
                #attributes
                #methods
            #instantiation/object creation
            obj1= Email([args])
            obj2= Email([args])

            attributes-
                heading
                participants
                attachments
            methods-
                send()
                save_as_draft()

        What is Object?
            Object- Object in OOP represents real-world objects.
                -object is instance of class
                ex. Email,Man, Student,Employee etc
                Every object has two properties
                    1. Attributes(Data) - heading,subject,name.recipient list
                    2. Behaviours(Action)/Methods - Sending, Adding attachments
                we can create multiple objects, and object-to-objects values of these will be different.
                    Obj_Email1-
                        heading-Taking Leave
                        to-xyz@gmail.com
                        attachments-form.pdf
                    Obj_Email2-
                        heading- Need help
                        to-abc@gmail.com
                        attachments-pic.jpg
    What is Constructor?
        - Special method used for initializing objects with attributes
        - It is __init__() method
        - First argument is 'self'
        Types of constructor-
            1. Parameterized constructor-pass parameter to method arg1,arg2..
            2. Non-Parameterized constructor- no parameters,only self present
            3. Default constructor

        "self"- self is variable which contains the memory reference of current object.

    How OOP works?
        1. Memory allocation for object
        2. Memory reference returned to the object
        3. Memory reference automatically passed inside constructor(self variable).
        4. Constructor creates/initialize variables at that memory referece
    
    How to access class members?
        class members- Attributes(variables)+ Actions(methods) present inside the class called class members.

        We can access these variables using object outside the calss.
        Syntax-
            Accessing attribute- obj_name.variable_name
            Accessing method- obj_name.method_name()

"""

class Employee:
    # constructor 
    # Parameterized constructor
    def __init__(self,name,emp_id):
        # attributes
        self.name = name
        self.emp_id = emp_id

    # method
    def display(self):
        print(f"Name of employee is {self.name} and employee id- {self.emp_id}")


emp1 = Employee('Gautam','001')
emp2 = Employee('Saanvi','002')

print(type(emp1)) # <class '__main__.Employee'>
print(emp1.__dict__)
print(emp1.name) # accessing attribute
emp2.display() # accessing method


class Animal:
    #Non-Parameterized constructor
    def __init__(self):
        self.name = 'Dog'

obj1 = Animal()
obj1
print(obj1.__dict__)

#without constructor: object can't be created
class Animal:
    #default constructor
    # no init methods so default constructor will call
    pass

obj_animal = Animal()
print(obj_animal.__dict__) # {} empty dict

"""
    Build-in class functions-
        1. getattr(obj_name, attribute_name)
        2. setattr(obj_name, attribute_name, new_value)
        3. deltattr(obj_name, attribute_name)
        4. hasattr(obj_name, attribute_name)
"""

class Child:
    def __init__(self,name,age):
        self.name = name
        self.age = age

obj_child_1 = Child('Saannvi',5) 
obj_child_2 = Child('Devansh',2)
print(getattr(obj_child_1,'name')) # Saanvi
setattr(obj_child_1,'name',"Saanvi Patil")
print(getattr(obj_child_1,'name')) # Saanvi Patil

print("Before deletion",obj_child_1.__dict__)
delattr(obj_child_1,'age')
print("After deletion",obj_child_1.__dict__)

print(hasattr(obj_child_1,'age'))
print(hasattr(obj_child_2,'age'))


"""
    Built-in class attributes-
        1. __dict__: Dictionary containing class's namespace
        2. __doc__: Class documentation string
        3. __name__: Class name
        4. __module__:Module name in which class is defined
        5. __bases__: List of base classes
"""

class Employee:
    ''' This is employee class for mainitaining data '''
    def __init__(self,name,emp_id):
        # attributes
        self.name = name
        self.emp_id = emp_id

    # method
    def display(self):
        print(f"Name of employee is {self.name} and employee id- {self.emp_id}")


emp1 = Employee('Gautam','001')
emp2 = Employee('Saanvi','002')

print(Employee.__doc__) # docstring
print(Employee.__dict__)
print(Employee.__name__) # Employee
print(Employee.__module__) #__main__

"""
    Instance variables & Instance methods
        Types of Variables
            1. Instance variables
                - Variables made for particular instance
                - Separate copy is created for every object
                - Values of variables differs from object-to-object.
                - Modification in one object won't affect other objects
                
                Creating instance variables
                    - Using constructor
                    - Using instance method
                    - Outside class

            2. Class variables
                - Variables made for entire class(All objects) are called class variables
                - Only one copy is created and distributed to all objects
                - Modification in class variable impact on all objects

        Class Method:
            - Method which works on class variables
            - First argument is class reference i.e 'cls'
            - Made using decorator '@classmethod'

        Instance Methods:
            1. setter method(mutator)- set values of instance variables
            2. getter method(accessor)- get values of instance variables
        
        Static Methods:
            - Methods which perfoms operations on external data
            - It can also perform operations on class data
            - No need to pass object or class reference
            - Created using decorator '@staticmethod'
"""

class Student:
    def __init__(self,name, marks) -> None:
        # Instance variables
        self.name = name
        self.marks = marks
    # instance method
    def display(self):
        print(self.name, self.marks)


stu_obj1 = Student('Yogesh',70) 
stu_obj2 = Student('Pravin',80) 
stu_obj3 = Student('Manish',85) 

stu_obj2.display()


# Example of class variable & class method
class Employee:
    company_name = 'Nitor' # class variable
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    # class method    
    @classmethod
    def get_company_name(cls):
        cls.company_name = 'Wipro' # modified name here
        print(f"Comapny name is : {cls.company_name}")

emp_obj1 = Employee('Ajay',30000)
emp_obj2 = Employee('Vijay',40000)

print(Employee.company_name) # Nitor
print(emp_obj1.company_name)

Employee.company_name = "NIPL"
# modify class variable value
print(Employee.company_name) # NIPL

Employee.get_company_name() # NIPL


# Example of setter and getter methods
class Employee:
    # setter method
    def setName(self,name):
        self.name = name

    # getter method
    def getName(self):
        print("The Name is:",self.name)


e1 = Employee()
e2 = Employee()

e1.setName("Gautam")
e2.setName("Snehal")
print(e1.__dict__)
print(e2.__dict__)

e1.getName()
e2.getName()


# Example of static method
class Bank:
    bank_name = 'SBI'
    rate_of_interest = 11.25

    # static method
    @staticmethod
    def simple_interest(princ_amt,yrs):
        Bank.bank_name = "ICICI"
        si = (princ_amt*yrs*Bank.rate_of_interest)/100
        print(f"Simple interest for bank {Bank.bank_name} is:{si}")

Bank.simple_interest(10000,3)
print(Bank.bank_name) # ICICI- we can change value of class variable in static method


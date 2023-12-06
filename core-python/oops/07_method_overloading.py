"""
    Method Overloading:
        When a class contain two or more methods with same name but different 
        behaviour is called as method overloading.
"""

class Addition:
    def add(self,a,b):
        print("Addition of two no. is:",a+b)

    def add(self,a,b,c):
        print("Addition of three no. is:", a+b+c)

a1 = Addition()
a2 = Addition()

# a1.add(1,2) # TypeError: add() missing 1 required positional argument: 'c'
# In python last method is called by default & python not support purely method overloading
a2.add(1,2,3)

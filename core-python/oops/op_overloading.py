"""
Operator Overloading-
    - When same operator behaves differently depending on values
    - You can assign a new meaning to operators also and you can extend functionality of operators.
    - You can change default behaviour of operator using over-riding

 Consider '+' operator
    10+20 = 30
    'hello'+'world' = helloworld
    [1,2,3]+[4,5,6] = [1,2,3,4,5,6]
"""

num1 = 20
num2 = 40
num3 = 60
print(num1+num2) # 60
print(num1.__add__(num2)) # 60
print(int.__add__(num1,num2))

# How it works internally
# step 1: Check datatype of left operand. # int
# step 2: go in that class
# step 3: call __add__() function


class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def __add__(self,other):
        total = self.pages+other.pages
        return Book('All books',total)
    
    def __str__(self):
        return str(self.pages)

b1 = Book("Do Epic Shit",300)
b2 = Book("Inner Engineering",500)
b3 = Book("Inner Engineering I",400)

# print(b1)

# print("Total no.of pages",b1.pages+b2.pages)
print("Total no.of pages",b1+b2+b3)


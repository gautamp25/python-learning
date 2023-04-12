# A function that takes
#  another function as an input and add some addition functionality 
# and return it.

def decor(func):
    def inner():
        print("inner Called")
        func()
    return inner

def print_greet():
    print("Hello There")
    print("Hello There")

# print_greet()
msg= decor(print_greet)
msg()
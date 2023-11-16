def make_printer(msg):
    print(msg)
    msg = "hi there"
    print(msg)

    def printer():
        print(msg)

    return printer


myprinter = make_printer("HEY")
myprinter()
myprinter()
myprinter()

def make_counter():

    count = 0
    def inner():
        # nonlocal count
        count += 1
        return count

    return inner


counter = make_counter()

c = counter()
print(c)

c = counter()
print(c)

c = counter()
print(c)
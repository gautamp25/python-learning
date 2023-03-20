def decorator_func(func):
    def wraper_func():
        print("wrapper_func worked")
        return func()
    print("Decorator_func worked")
    return wraper_func

def show():
    print("Show worked")
decorator_show = decorator_func(show)
decorator_show()

print("*"*10)


@decorator_func
def display():
    print("Display worked")

display()

l=[1,2,3,4,5]
val = [x&1 for x in l]
print(val)

print(5&1)
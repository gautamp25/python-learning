from re import A


my_tuple = (1,2,3,4)
my_dict = {}
my_dict[my_tuple] = "a"
print(my_dict)

def fib(n):
    a,b = 0,1
    while a<n:
        yield a
        a,b = b, a+b


x=fib(5)
print(x)

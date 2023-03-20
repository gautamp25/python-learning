def square():
    i = 1

    while True:
        yield i*i
        # print(f"I -{i}")
        i+=1
        # print(f"I after + -{i}")

for num in square():
    if num>200:
        break
    else:
        print(num)


# Example 2 * args & **kwargs
# We use this, when we have doubts about number of arguments passed in function then 
# *args- non keyword arguments
# **kwargs - keyword arguments like key & name
def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
  
  
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

print("======Example 3========")

def fib(number):
    a,b = 0,1
    while a< number:
        yield a
        a,b = b, a+b
x=fib(5)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print('+++++++++++++')
for j in fib(10):
    print(j)


        

l1=[1,0,4,0,3,0,2,0,0,1,-1]
# shift_zero = [f"{d.append(y)}" for d in l1 if d!=0  for y in l1 if d>0] 
# s2= [f for f in l1 if f<1]
# print(s2)
# print(shift_zero)
# shift_zero.append(list(s2))
# print(shift_zero)
l2=[1,1,2,2]
l1.extend(l2)
print(l1)
# def fn(l1):
data=[]
d1=[]
d3= []

for d in l1:
    if d!=0:
        data.append(d)
    else:
        d1.append(d)
        
# b= data.extend(d)
    # return b
    
# b=fn(l1)
print(data.extend(d1))


# decorator
def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$$$")
        func()
        print('executing...')
    return wrap

@decor
def sayhi():
    print("Hi")

sayhi()

# closure
def outer(x):
    def inner():
        print(x)
    return inner

outer(6)()


print('==========================')

def outer1():
    a=7
    def inner1():
        nonlocal a
        print(a)
        a+=1
        print(a)
    return inner1


outer1()()




# functions of list
list_a= [1,2,3,4,5]
list_b= [7,8,9,0]
list_a.extend(list_b)
print(list_a)


# functions of Dictionary

d1 = {'name':'gautam','job':'Software Engg','age':32}
d2 = {'name':'sp','job':'Software Engg','age':30}
# for d in d1.items():
#     print(d)
seq = {'a', 'b', 'c', 'd', 'e'}
res = dict.fromkeys(seq)
print(res)
print(d1.clear())

a = 100
print(repr(a))
print(type(repr(a)))
print("*"*10)

def sum(a,b=5):
    total = a*b
    print(total)
sum(4,)

def total(*args):
    t = 0
    for a in args:
        t += a
    print(t)

total(1,2,3,4,5) # 15

def show(**kwargs):
    print(kwargs)

show(a=1,b=2,c=3) # {'a': 1, 'b': 2, 'c': 3}
l = [1,4,6,9]
print('l',l.__sizeof__())
l1 = [4,5,6]
l.extend(l1)
print(l)
print(l.pop())
# print(f"L-{l}")
# l.remove(3)
# print(l)
print(l.count(1))

t= 1,4,6,9
print('t',t.__sizeof__())
print(type(t))
print(t[2])
# t[4] = 10
print(t)
print("+++++++++++++")
l4= [1,2,3,4,5,6]
print(l4[:])
print(l4[-7:])
print(l4[0:6])
print(l4[:])

num = [2,3,4,5]
print(sum(num,100))

x = [1,2,3]
y = x
y[1] = 4
print(x)

# Concatenation and Replication
print([1,2,3]+['a','b','c','d'])
print(['X', 'Y', 'Z'] * 3)

my_list = [1, 2, 3]
my_list += ['A', 'B', 'C']
print(my_list)

# Getting the index in a loop with enumerate()
furniture = ['table', 'chair', 'rack', 'shelf']
for index, item in enumerate(furniture):
    print(f'Index- {index} value -{item}')

# Loop in Multiple Lists with zip()
furniture = ['table', 'chair', 'rack', 'shelf','tpoy']
price = [100, 50, 80, 40]

for item, amount in zip(furniture,price):
    print(f"The {item} costs-${amount}")

# The Multiple Assignment Trick
furniture = ['table', 'chair', 'rack', 'shelf']
table,chair,rack,shelf = furniture
print(table,chair)

# insert()
# insert adds an element to a list at a given position:
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.insert(2,'bed')
print(furniture)

""" Removing Values
    del()
    del removes an item using the index:
"""
furniture = ['table', 'chair', 'rack', 'shelf']
del furniture[2]
print(furniture)

del furniture[1]
print(furniture)

"""
remove()
remove removes an item with using actual value of it:

-Removing repeated items
    If the value appears multiple times in the list, only the first instance of the value will be removed. 
"""
furniture = ['table', 'chair', 'rack', 'shelf']
furniture.remove('chair')
print(furniture)

"""pop()
By default, pop will remove and return the last item of the list. 
You can also pass the index of the element as an optional parameter:
"""
animals = ['cat', 'bat', 'rat', 'elephant']
nums = [2, 5, 3.14, 1, -7]
# animals.sort()
# print(animals)
b=sorted(animals)
print(b)
print(id(b),id(animals))

print(animals.pop())
print(animals)

print(animals.pop(0))
print(animals)

print(2**3)

a=10
b=15
print(a&b)

l1 = [1, 2, 3]
l2 = [2, 3, 4]
l3 = [3, 4, 5]
print(l1+l2+l3)


# Python Comprehensions
# List Comprehensions are a special kind of syntax that let us create lists out of other lists,
#  and are incredibly useful when dealing with numbers and with one or two levels of nested for loops.
names = ['gautam','saanvi','devansh','snehal']
new_name_list = [n for n in names]
print(new_name_list)
print(id(names),id(new_name_list))

print(15%3)

# Set comprehension

b = {"abc", "def"}
print({s.upper() for s in b})
# o/p {"ABC", "DEF"}

# Dict comprehension

c = {'name': 'Pooka', 'age': 5}
print({v: k for k, v in c.items()})
# o/p  {'Pooka': 'name', 5: 'age'}

# A List comprehension can be generated from a dictionary:

c = {'name': 'Pooka', 'first_name': 'Oooka'}
print(["{}:{}".format(k.upper(), v.upper()) for k, v in c.items()])
# o/p ['NAME:POOKA', 'FIRST_NAME:OOOKA']

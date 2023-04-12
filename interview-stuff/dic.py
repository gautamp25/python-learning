# sourcery skip: use-dictionary-union
print("Drawbacks of '=' while dict copy")
d1 = {'a':1, 'b':2, 'c':3}
print(d1)
d2 = d1
print(d2)
del d1['b']
print("After delete D1",d1)
print("After delete D2",d2)
print(id(d1))
print(id(d2))

print("Using copy() function")
d1 = {'a':1, 'b':2, 'c':3}
print(d1)
d2 = d1.copy()
print(d2)
del d1['b']
print("After delete D1",d1)
print("After delete D2",d2)
print(id(d1))
print(id(d2))

"""
items()

The items() method gets the items of a dictionary and returns them as a Tuple:
"""
pet = {'color': 'red', 'age': 42}
for item in pet.items():
    print(item)

# Using the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary, respectively.
pet = {'color': 'red', 'age': 42}
for key,value in pet.items():
    print(f'Key-{key} and value-{value}')

# get()

# The get() method returns the value of an item with the given key. If the key doesn’t exist, it returns None:

wife = {'name': 'Rose', 'age': 33}
print(wife.get('name'))


# You can also change the default None value to one of your choice:
print(wife.get('husband'))
print(f'She is deeply in love with {wife.get("husband", "lover")}')

# Removing Items
# pop()

# The pop() method removes and returns an item based on a given key.

wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
wife.pop('age')
# 33
print(wife)
# {'name': 'Rose', 'hair': 'brown'}

# popitem()

# The popitem() method removes the last item in a dictionary and returns it.

wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
wife.popitem()
# ('hair', 'brown')
print(wife)
# {'name': 'Rose', 'age': 33}

# del()

# The del() method removes an item based on a given key.

wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
del wife['age']
print(wife)
# {'name': 'Rose', 'hair': 'brown'}

# clear()

# The clear() method removes all the items in a dictionary.

wife = {'name': 'Rose', 'age': 33, 'hair': 'brown'}
wife.clear()
print(wife)
# {}


# Merge two dictionaries

# For Python 3.5+:

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)
x = list(dict_a)
print(x)
*y, =dict_a.keys()
print(y)
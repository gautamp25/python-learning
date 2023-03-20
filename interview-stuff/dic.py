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
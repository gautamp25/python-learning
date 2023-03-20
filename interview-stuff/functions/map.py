fruit = ['Apple', 'Banana', 'Pear']
map_obj = map(lambda s: s[0] == "A", fruit)
print(list(map_obj))
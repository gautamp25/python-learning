"""
dictionary preserve the order the items added
"""
my_dict= {}
my_dict['austin'] = 9015
print(my_dict)
my_dict['boston'] = 9512
print(my_dict)
my_dict['boston'] = 1001
print(my_dict)
my_dict['adem'] = 9600
print(my_dict)
# delete element
del my_dict['adem']
print(my_dict)
print(my_dict.get('adem'))
print(len(my_dict))
# clear/empty dictionary
# my_dict.clear()
# del my_dict
print(my_dict)

x= [1,2,3,4]
print(x.pop(3))

b = 1,2,
print(type(b))


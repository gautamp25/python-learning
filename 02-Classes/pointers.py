num1 = 11
num2 = num1
print("Before num2 value is updated")
print("num1=",num1)
print("num2=",num2)

print("num1 points to:", id(num1))
print("num2 points to:", id(num2))

print("======================")

num2 = 22
print("After num2 value is updated")
print("num1=",num1)
print("num2=",num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# IMP-Integer are immutable

print("\n***********DICTIONARY***********")
# Dictionary
dict1 = {
    'value':11
}
dict2 = dict1
print("\nBefore value is updated:")
print("dict1=", dict1)
print("dict2=", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22
print("\nAfter value is updated:")
print("dict1=", dict1)
print("dict2=", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# IMP- Dictioaries can be changed

# Nodes in linked list are going to opeate very much like Dictionary

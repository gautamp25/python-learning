my_string = 'ab@c/def$ij'
opt='ji@f/edc$ba'
for i in range(len(my_string)-1):
  print(my_string[i])


  my_dict = {1:'a', 2:[],3:{4: {5: {}}}}
  print(len(my_dict))
# count = 0

d = {1:'a', 2:[],3:{4: {5: {}}},4:'qbc'}

# correct way
def count_nested_dicts(d):
    count = 0
    for value in d.values():
        if isinstance(value, dict):
            count += 1
            count += count_nested_dicts(value)
    return count

print(count_nested_dicts(d))

# =========================
my_string = 'ab@c/def$ij'

# Convert string to list of characters
my_list = list(my_string)

# Initialize variables for start and end indices of alphabetic characters
start = 0
end = len(my_list) - 1

# Loop over the characters in the list
while start < end:
    # If start character is not alphabetic, move to the next character
    if not my_list[start].isalpha():
        start += 1
    # If end character is not alphabetic, move to the previous character
    elif not my_list[end].isalpha():
        end -= 1
    # If both start and end characters are alphabetic, swap them
    else:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1
    print(my_list)

# Convert list of characters back to string
my_string = ''.join(my_list)

# Print the reversed string
print(my_string)  # Output: ij@c/fed$ba
# ----------------------------------------
import re

my_string = 'ab@c/def$ij'

# Use regular expression to match alphabetic characters
matches = re.findall(r'[a-zA-Z]', my_string)

# Reverse the order of the matches
matches.reverse()
print(matches)
print(lambda m: matches.pop(0), my_string)

# Replace the alphabetic characters in the string with the reversed characters
my_string = re.sub(r'[a-zA-Z]', lambda m: matches.pop(0), my_string)

# Print the reversed string
print(my_string) 

# ===================================


# def decorator_fuc(func,a):
#   def wrapper_func():
#     print(a)
#     print("In wrapper func")
#     return func()
#   return wrapper_func 

# # @decorator_fuc
# def greet():
#   print("Hello there Good Afternoon")

# my_decorator = decorator_fuc(greet,a=3)
# my_decorator()


# class Employee:
  
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
    
#   @staticmethod
#   def display():
#     print()

#   def display(self):
#     print("")

#   def display_details(cls):
#     print(f"My name is {cls.name}")
    


# obj1 = Employee("Shyam",20)
# Employee.display_details()

my_string = 'ab@c/def$ij'
opt='ji@f/ed'
for i in range(len(my_string)-1):
  print(my_string[i])
  
    


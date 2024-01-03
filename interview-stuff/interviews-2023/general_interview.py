# What is deep copy?
"""
    Deep copy- A deep copy refers to the creation of new object that is a copy of another object, including all the objects referenced by it. 
    The key characteristic of deep copy is that it creates a completely independent copy of the original object along with all the objects nested within it.
    Changes made to the original object or its nested objects do not affect the deep copy, and vice versa.

"""
import copy

# Original list with nested lists
original_list = [1, 2, [3, 4], 5]

# Create a deep copy
deep_copy_list = copy.deepcopy(original_list)

# Modify the original list
original_list[2][0] = 'X'

deep_copy_list[2][1]=10

# Display the original and deep copy
print("Original List:", original_list)
print("Deep Copy List:", deep_copy_list)

print(id(original_list))
print(id(deep_copy_list))
print()
print(id(original_list[0]))
print(id(original_list[1]))
print(id(original_list[2]))
print(id(deep_copy_list[2]))
print(id(original_list[2][0]))

# output:
# Original List: [1, 2, ['X', 4], 5]
# Deep Copy List: [1, 2, [3, 4], 5]

# In this example, the deepcopy() function creates a new list (deep_copy_list) that is a deep copy of original_list.
# Even though we modify the nested list within original_list, the deep copy remains unaffected.

# Use Deep Copy When:
"""
1. Nested Structures with Mutable Objects:
        When your data structure contains nested structures (e.g., nested lists or dictionaries) with mutable objects (e.g., lists or other objects that can be modified),
        and you want to create a fully independent copy of the entire structure.

    Example:
    import copy

    original_data = {'a': [1, 2, 3], 'b': {'x': 10, 'y': [20, 30]}}
    deep_copy_data = copy.deepcopy(original_data)

2. Preventing Side Effects:

    When you want to avoid unintentional side effects caused by modifications to the copied structure affecting the original structure.

Example:

    import copy

    original_list = [1, 2, [3, 4], 5]
    deep_copy_list = copy.deepcopy(original_list)
"""
    
# what is shallow copy?
"""
    In Python, a shallow copy refers to the creation of a new object that is a copy of another object, but it only copies the top-level structure of the object, not the objects nested within it.
    In a shallow copy, the new object is a separate entity, but it still contains references to the same nested objects as the original object.

The copy module in Python provides the copy() function to perform shallow copies.
Additionally, for sequences like lists, you can use the slicing notation [:] to create a shallow copy.
"""

import copy

# Original list with nested lists
original_list = [1, 2, [3, 4], 5]

# Create a shallow copy
shallow_copy_list = copy.copy(original_list)

# Modify the original list
original_list[2][0] = 'X'
original_list[0] = 100

shallow_copy_list[2][1]=7
# Display the original and shallow copy
print("Original List:", original_list)
print("Shallow Copy List:", shallow_copy_list)

print("Original List ID:",id(original_list))

print("Shallow Copy List ID:",id(shallow_copy_list))

print(id(original_list[0]))
print(id(shallow_copy_list[0]))
print("*"*10)
print(id(original_list[0]))
print(id(original_list[1]))
print(id(original_list[2])) # 1935640029120
print(id(shallow_copy_list[2])) # 1935640029120

note= original_list[:]
original_list[2][0] = 'y'
note[2][0]='G'
print(note)
print(original_list)



# Use Shallow Copy When:
"""
1. Top-Level Independence is Sufficient:
        When you only need a new object that is independent at the top level (i.e., modifying the top-level structure of the copied object should not affect the original).

    Example:

    import copy

    original_data = {'a': [1, 2, 3], 'b': {'x': 10, 'y': [20, 30]}}
    shallow_copy_data = copy.copy(original_data)

2. Performance Considerations:

    When performance is a concern, as shallow copy is generally faster than deep copy. If you don't need full independence for nested structures, a shallow copy may be more efficient.

    Example:

    original_list = [1, 2, [3, 4], 5]
    shallow_copy_list = original_list[:]

3. Memory Considerations:

    When dealing with large datasets and memory is a concern, as a shallow copy may use less memory than a deep copy.

    Example:
    import copy

    original_data = {'a': [1, 2, 3], 'b': {'x': 10, 'y': [20, 30]}}
    shallow_copy_data = copy.copy(original_data)
"""

# Dictionary program
my_dict = {
    "key1":[1,2,3],
    "key2":[4,5,6],
    "key3":"hello",
    "key4":[7,8,9,10]
}
# using dict comprehension
new_dict = {key:val for key,val in my_dict.items() if isinstance(val, list) and all(isinstance(x, int) for x in val) and sum(val)>14}
print(new_dict)



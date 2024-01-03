# Cognizant interview 11:00 AM to 11:30 AM
"""1.list and tuple difference.
2.Swap the dict.
    d1= {'b': 10, 'a': 5, 'c': 90}
    d2 = {}
    for key,val in d1.items():
        d2[val]=key
    print(d2)
3. What is slice in python?
4. get te last 3 char from str1 i.e kaj 
    str1="pankaj"
    print(str1[3:6])# kaj

4.update list ele in tuple. tuple1 =(1,2,[22,33])
    tuple1 =(1,2,[22,33])
    tuple1[2][0]=200 # 
5. Merge the dict
   d = [{'b': 10, 'a': 5, 'c': 90}, {'b': 78, 'a': 45}, {'a': 90, 'c': 10}]

    merged_dict = {}
    for sub_dict in d:
        print(sub_dict)
        merged_dict.update(sub_dict)

    print(merged_dict)
t1=[1,2,3] count commos.
t1 = ['1', '2', '3']

# Convert the list to a string
list_as_string = str(t1)

# Count the commas in the string representation of the list
comma_count = list_as_string.count(',')

print(comma_count)

"""
# What is slicing in python?
"""
In Python, a "slice" refers to a way to extract a specific section of a sequence type (like a list, tuple, string, etc.)
by specifying a range or specific indices.
It's done using the slicing notation [start:stop:step].

    start: The index where the slice begins (inclusive).
    stop: The index where the slice ends (exclusive).
    step: The step or interval between elements.

For example:

my_list = [1, 2, 3, 4, 5]

# Grabbing a slice of the list
slice_result = my_list[1:4]  # Starts at index 1, ends at index 3 (4 is exclusive)
print(slice_result)  # Output: [2, 3]

If any of the values in the slicing notation are omitted, Python uses default values: start defaults to the beginning of the sequence, stop defaults to the end of the sequence, and step defaults to 1.


my_list = [1, 2, 3, 4, 5]

# Omitting start and stop indices
slice_result = my_list[2:]  # Starts at index 2 till the end
print(slice_result)  # Output: [3, 4, 5]

# Using negative indices
slice_result = my_list[:-2]  # Starts from the beginning till the second last element
print(slice_result)  # Output: [1, 2, 3]

# Using step
slice_result = my_list[::2]  # Returns every second element
print(slice_result)  # Output: [1, 3, 5]

Slicing is a powerful feature in Python that allows you to manipulate sequences efficiently by working with subsets of data without modifying the original sequence.
"""
t1=[1,2,3,1]
t1_str = str(t1)
print(t1_str)

print(t1_str.count(','))

d = [{'b': 10, 'a': 5, 'c': 90}, {'b': 78, 'a': 45}, {'a': 90, 'c': 10}]

merged_dict = {}
for sub_dict in d:
    # print(sub_dict)
    merged_dict.update(sub_dict)

print(merged_dict)
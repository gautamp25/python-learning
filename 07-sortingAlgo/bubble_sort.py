# Bubble Sort- Bubble out large number first
"""
The function should perform the following tasks:

    Accept a parameter my_list that represents the list of integers to be sorted.

    Iterate through the list from the last element to the first element. For each element i, perform the following steps:

        Iterate through the list from the first element to the element at position i - 1. For each element j, perform the following steps:

            Compare the element at position j with the element at position j + 1. If the element at position j is greater than the element at position j + 1, swap the two elements.

    Return the sorted list.
"""
"""
Pseudo code:
 for i in range(len-1,0,-1):
    for j in range(i):
        if j>j+1:
            swap
            j,j+1 = j+1,j
return []
"""

my_list = [5,3,6,4,1]
def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j]>my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list
print("Sorted list->", bubble_sort(my_list))
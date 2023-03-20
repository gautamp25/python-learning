# insert operation- linear 
# appending- constant time operation
# delete- O(n) linear runtime
# arrays are quite fast while accesing the value, reading values happens in constant runtime
# arrays are pretty bad at inserting and deleting both of which run in linear time.
# Linked list on other hand better
"""
space = N*M
when list is created the list doen't know anything about the size of list and how many elements going to store.
number = [] // here create a list and allocates a space of size n+1 since n=0 here. space is allocated for one element list
to start off,bcoz space allocated to for the list and space used by list are not same.

list resizing-
growth pattern of list type in python is 0 4 8 16 25 35 46 and so on
"""
number = []
print(len(number))
# number.append(2)
# number.append(200)
print(number)
number.extend([1, 2, 3]) # runtime has O(k) k represent no.of ele present in list that we're adding to existing list
print(number)

l1= []
l1.append(1)
l1.append(2)
l1.append(3)
print(l1)
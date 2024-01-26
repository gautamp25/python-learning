my_list = [11,3,23,7]
my_list.append(17)
print(my_list)
my_list.pop()
print("After pop",my_list)
my_list.pop(0)
print("After pop 0th index",my_list)

# Big O of list goes, end adding or removing is O(1) and for start removing and adding needs re-indexing so O(n)
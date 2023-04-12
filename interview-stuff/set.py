"""
A set is an unordered collection with no duplicate elements.
Basic uses include membership testing and eliminating duplicate entries. 
Set objects also support mathematical operations like union, intersection, difference, and symmetric difference


-Empty Sets
    When creating set, be sure to not use empty curly braces {} or you will get an empty dictionary instead. 
-remember that sets are unordered 
    There is no guarantee that when converting them back to a list, the order of the elements will be preserved.

"""

s1 = set([1, 2, 3])
print(s1)

s2 = {3, 4, 5}
print(s2)

s = {}
s= set()
print(type(s))

# set add() and update()
# Using the add() method we can add a single element to the set.
s = {1, 2, 3}
s.add(4)
print(s)

s.update([1,2,3,5,6])
print(s)

# set remove() and discard()
# Both methods will remove an element from the set, but remove() will raise a key error if the value doesn’t exist.
s = {1, 2, 3}
s.remove(3)
print(s)
s.discard(4)
print(s)

# set union()
# union() or | will create a new set that with all the elements from the sets provided.

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))  # or 's1 | s2'


# set intersection
# intersection or & will return a set with only the elements that are common to all of them.

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
print(s1.intersection(s2, s3))

# set difference
# difference or - will return only the elements that are unique to the first set (invoked set).

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.difference(s2))  # or 's1 - s2'
# {1}
print(s2.difference(s1))

# set symetric_difference
# symetric_difference or ^ will return all the elements that are not common between them.

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.symmetric_difference(s2))


#Remove duplicates

my_list = [1,2,3,4,2,3,5,4,6]
no_duplicates = []
[no_duplicates.append(items) for items in my_list if items not in no_duplicates]
print(no_duplicates)

from timeit import timeit
def no_duplicates(list):
    no_duplicates = []
    [no_duplicates.append(items) for items in list if items not in no_duplicates]
    return no_duplicates
print(timeit('no_duplicates([1,2,3,4,2,3,5,4,6])',globals=globals(),number=1000))

print(timeit('list(set([1,2,3,4,2,3,5,4,6]))',number=1000))

from timeit import timeit
def in_test(iterable):
    for i in range(1000):
            if i in iterable:
                    pass
print(timeit('in_test(iterable)', setup="from __main__ import in_test; iterable = list(range(1000))", number=1000))


from timeit import timeit
def in_test(iterable):
    for i in range(1000):
            if i in iterable:
                    pass
print(timeit('in_test(iterable)', setup="from __main__ import in_test; iterable = set(range(1000))", number=1000))

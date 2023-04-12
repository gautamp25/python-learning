
"""
Dictionary key is immutable

Dictionary vs Sets vs Tuples

Tuple-
    1. Tuple is collection that is ordered and unchangeble and is indexed.
    2. Allows duplicates items
Set-
    1. Set is collection that is unordered & unindexed
    2. No duplicate items

Dictionary-
    1. Dictionary is collection that is unordered and changeble and indexed.
    2. No duplicate keys but values can be duplicated

1. Dictionaries,lists and tuples give better control in accessing the data
2. Dictionaries and sets have faster access times compared to lists and tuples
3. Key order depends on insertion order


Hash Table-
    - A hash table's goal is to keep the data evenly distributed across the table.
    - In dictionary implementation the goal is to keep at least one-third of hash table empty.
    - Hashable objects that compare equal:
        1. Will need to have the same hash value consistently
    - Dictionary keys must be immutable e.g str,bytes.numeric

    - Cells in hash table are often called buckets
    - In python dict-hash table there is a bucket for each item which contains the hash value,the item key and the item value
    - Python has built in Hash function.  


"""
d = {'a':'apple','b':'berry','c':'cherry'}
# Access value from dictionary
print(d.get('a','not found'))
print(d.get('d','not found'))

# List all keys
print(d.keys())

# List all values
print(d.values())

# List both keys and their value
print(d.items())

# Find the maximum value in the dictionary
sal_info = {'austin': 9015, 'boston': 1001, 'adem': 9600}
print(max(sal_info,key=sal_info.get))

# Return the value associated with key(removes key-value pair from dict)
d['g']='grapes'
print(d)
print(d.pop('g'))
print(d)

# sort
print(sorted(sal_info.keys()))
print(sorted(sal_info.values()))

# Loop
for i in range(10):
    if i==5:
        continue
        print("I here")
    else:
        print(i)
else:
    print('Here')
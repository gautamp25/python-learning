# List of all the keys in dictionary
print("Appraoch-1,2")
dct = {'a':1,'b':2,'c':3}
all_keys = list(dct)
print(all_keys)

all_keys = list(dct.keys())
print(all_keys)

print("unpacking operator")
x= [*dct]
print(x)

p= [*dct.keys()]
print(p)

print("Using keys function")
y = dct.keys()
print(y)
print([k for k in y])


print("Using Iterable Unpacking operator")
*z, = dct.keys()
print(z)
*k,=dct
print(k)

lst = [1,2,3,4,5]
print(lst[-1])
print(lst[:-1])

def reverseList(lst):
    if not lst:
        return []
    return [lst[-1]]+ reverseList(lst[:-1])

print(reverseList(lst))

lst=[1,2,3,4,5]
print(lst[len(lst)//2:])
print(5/2)
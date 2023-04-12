# Mutable objects- List,Set,Dictionary,Bytearray
l = [1,2,3,4]
print("Before modification:",l)
l[2]=5
print("After modification:",l)

# Immutable objects - Tuple,frozenset,bytes,range,and all
#  fundamental objects are immutable(int,float,complex,string,boolean)
t = (1,2,3,4)
print("Before modification:",t)
t[2]=5
print("After modification:",t) # TypeError: 'tuple' object does not support item assignment

s = "abcd"
# s[0] = 'x'
print(id(s))
print(s) # TypeError: 'str' object does not support item assignment
s= 'xyz'
print(s)
print(id(s))
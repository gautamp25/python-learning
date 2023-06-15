"""
Omega- Best case
Theta- Average case
Omicron or O - worst case

When you talk about big O, always talk abt worst case

O(n) (Proportional)- O(n) is always going to be a straight line.

O(n^2) (Loop within a loop) - Lot less efficient from a time complexity standpoint.

O(1) (Constant)- Constant time. when n increases number of operations will remain constant.
It's  ost efficient big O

O(log n) (Divide and Conquer)- 2^3 = 8 i.e log2^8 =3
It is far more efficient than O(n) or O(n^2)

Big O for Lists - Adding or removing item is O(1) while inserting in-between 
require re-arrange so, time is O(n)

www.bigocheatsheet.com

"""
# O(n)
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)
print("****")
# Drop constant 
def print_items(n):
    for i in range(n):
            print(i)
    for j in range(n):
            print(j)

print_items(10)
# n+n = 2n => O(n)
print("****O(n^2)****")
# O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
                print(i,j)

print_items(10) # n*n =n^2

# ticky question- Its not O(n) This is O(a) and O(b) = O(a+b)
def print_item(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
            print(j)
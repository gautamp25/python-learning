l1 = [1,2,3,4]
x = list(map(lambda a:a**3,l1))
y = map(lambda b:b**2,l1)
print(list(y))
print(x)

# call by value
a = "gtm"
b = 'gtm'
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
c = "ptl"
print(id(c))
print(c)

e = 'a'
e = 'b'
print(id(e))
print(e)

s1 = 'Gautam'
def change(s1):
    s1 = "Gautam Patil"
    print("Inside",s1)

change(s1)
print("Outside",s1)

# call by Reference
def add_more(list):
    list.append(50)
    print("Inside Function",list)

my_list = [10,20,30]
add_more(my_list)
print(my_list)

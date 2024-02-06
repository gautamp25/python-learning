def append(ele, lst=[]):
    lst.append(ele)
    return lst
f_lst=append(10)
print(f_lst, end=" ")

s_lst=append(30)
print(s_lst)

my_string = "Python is Beutiful"
# o/p = "Beutiful is Python"
print(my_string.split(" ")[::-1])
print(" ".join(my_string.split(" ")[::-1]))


num = [1,2,3,4,5]
print(num[1:6:-1])
print(num[-1])
num[-1] = 6 
print(num)

char = ['p','y','t','h','o','n']

for char[-1] in char:
    print(char[-1])

# 3.33
# 3 is floor value and .33 i.e 4 is ceil Value

print(-10//3) # -4
print(10//3.0) # 3.0 if contains float value then ans will be float. to avoid data loss problem

list = ["alfa", "bravo", "charlie", "delta", "echo"]

print(list[10:])
print (list[-7:]) 

l = [1,2,3,4] # Iterable
a = iter(l) # iterator
print(a)
print(next(a))
print(next(a))

# same priority for exponent operator **
#  Associativity in case of conflicts- Left - Right(normal associativity) & Right-Left
# Exponetial operator follows Right to Left associativity.
print(2**3**2)#3*3->2*2*2*2*2*2*2*2*2
print('2**5 evaluates to: ', 2**5) # 2*2*2*2*2
print(2**3**3)
# even no.of slashes
print("/\\/\\/\\/\\/\\")
print("/\\")

name = "gautam"
print(name[1:6:-2]) # blank output
# -2 decide the direction here it is negative and 6 will not get there

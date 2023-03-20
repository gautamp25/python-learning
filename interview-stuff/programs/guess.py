# 1  what will the output
from tkinter import N


x = 0
while x<=18:
    x = x+3
print(x)
# 2
l1 = [1,3,4,5]
print(l1[::1])
for i in l1[::1]:
    print(i,end="")

# 3
def factorial(N):
    if N ==1:
        return N
    else:
        return N*factorial(N-1)

print(factorial(5))

s = 'linkedin'
print(s.find('e'))
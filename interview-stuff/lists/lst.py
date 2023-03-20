l = [1,4,6,9]
print('l',l.__sizeof__())
l1 = [4,5,6]
l.extend(l1)
print(l)
print(l.pop())
# print(f"L-{l}")
# l.remove(3)
# print(l)
print(l.count(1))

t= 1,4,6,9
print('t',t.__sizeof__())
print(type(t))
print(t[2])
# t[4] = 10
print(t)
print("+++++++++++++")
l4= [1,2,3,4,5,6]
print(l4[:])
print(l4[-7:])
print(l4[0:6])
print(l4[:])

num = [2,3,4,5]
print(sum(num,100))

x = [1,2,3]
y = x
y[1] = 4
print(x)
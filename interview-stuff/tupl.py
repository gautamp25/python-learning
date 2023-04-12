a = (1,2,3)

b = (4,5,6)
c = a + b
# print("Tuple A",a)
print("ID of A",id(a))
# print("Tuple b",b)
print("ID of b",id(b))
print(c)
# print("Tuple C",c)
print("ID of C",id(c))
a = b+a
# print(a)
print(id(a))

# ---------------------
print("*"*10)

list_1 = [1,2,3]
print("Id of List_1", id(list_1))
list_2 = [4,5,6]
print("Id of List_2", id(list_2))
print(list_1+list_2)
# list_1.append(list_2)
list_1.extend(list_2)
print(list_1)
print("Extend",list_1)
list_3 = list_1
print("Id of List_3", id(list_3))

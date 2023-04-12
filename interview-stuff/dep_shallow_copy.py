import copy
l = [[1,2],[3,4]]
print("+++++Deep copy+++++")
print("Id of l1:",id(l))
print("First element id:",id(l[0]))
print("Second element id:",id(l[1]))
print('*'*30)
cp = copy.deepcopy(l)
print("Id of cp:",id(cp))
print("First element id:",id(cp[0]))
print("Second element id:",id(cp[1]))
print()
print(id(l))
print("Original:",l)
print(id(cp))
print("Copy obj:",cp)

cp[0][0]=10
print(cp)
print(l)
print("Change in original")
l[0][1]=11
print(cp)
print(l)
print()
print("+++++Shallow copy+++++")
print()
l1 = [[2,3],[4,5]]
print("Id of l1:",id(l1))
print("First element id:",id(l1[0]))
print("Second element id:",id(l1[1]))
print('*'*30)
sh = copy.copy(l1)
print("Id of sh:",id(sh))
print("First element id:",id(sh[0]))
print("Second element id:",id(sh[1]))
# print(id(l1))
# print("Original:",l1)
# print(id(sh))
# print("Shallow:",sh)

# sh[0][1]=45
# print(sh)
# print(l1)

ls = [10,20,30]
print(id(ls[0]))
print(id(ls[1]))
print(id(ls[2]))
print()
new_ls = copy.deepcopy(ls)
new_ls[0]=100
print(id(new_ls[0]))
print(id(new_ls[1]))
print(id(new_ls[2]))
print(new_ls)
print(ls)

print("===========")
l2 = [30,40,50]
print(id(l2[0]))
print(id(l2[1]))
print(id(l2[2]))
print()
new_l2 = copy.copy(l2)
new_l2[0]=100
print(id(new_l2[0]))
print(id(new_l2[1]))
print(id(new_l2[2]))
print(new_l2)
print(l2)





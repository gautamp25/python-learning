from functools import reduce

from importlib_metadata import version


# from functools import reduce
lst = [2,4,7,3]
print(reduce(lambda x,y:x+y,lst))
print("With initial value:" + str(reduce(lambda x,y:x+y,lst,4)))

# n = int(input("Enter no of rows"))
n = 5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")

    print()

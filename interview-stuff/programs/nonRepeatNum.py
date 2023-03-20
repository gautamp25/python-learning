def printNonRepeated(arr,n):
    if len(arr) == n:
        my_dict = {}
        for i in arr:
            if i in my_dict:
                my_dict[i] = my_dict[i]+1
            else:
                my_dict[i] = 1
        non_repeated = []
        for j in my_dict:
            if my_dict[j] == 1:
                non_repeated.append(j)
        return non_repeated
            
    

# arr = [10,20,40,30,10]
arr = [0, 9, 2, 3, 4, 8, 7]
print(printNonRepeated(arr,7))

d = {10:2,30:1,20:1,40:1,}
for i in d:
    if d[i] ==1:
        print(i)
    #  print(d[i])
def foo():
    n = 5
    arr = [10,20,40,30,10]
    new_list = []
    non_repeated = []
    for i in range(n):
        new_list.append(arr[i])
    return new_list
print(foo())

def printNonRepeated1(arr,n):
    my_dict = {}
    for i in range(n):
        if i in my_dict:
            my_dict[i] = my_dict[i]+1
        else:
            my_dict[i] = 1
    non_repeated = []
    for j in my_dict:
        if my_dict[j] == 1:
            non_repeated.append(j)
    return non_repeated
            
    

arr = [10,20,40,30,10]
print(printNonRepeated(arr,5))

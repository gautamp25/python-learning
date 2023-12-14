def all_nums():
    num_list = []
    num = 0
    while num<5:
        num_list.append(num)
        num+=1
    return num_list
   
print(all_nums())

def all_the_nums():
    num = 0
    while True:
        yield num
        num+=1

# for num in all_the_nums():
#     print(num)



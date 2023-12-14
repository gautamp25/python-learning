def square(num):
    num_list= []
    for i in range(1,num):
        num_list.append(i**2)
    return num_list

print(square(10))

# with generator function
def square_1(num):
    for i in range(1,num):
        yield i**2 

gen_obj=square_1(10)
print(gen_obj)
print(list(gen_obj))

print("*"*20)

# List comprehension 

my_list = [i**2 for i in range(1,10)]
print(my_list)

# generator expressions
"""
1. Create an iterator in a sinle line of code- still save memory
"""
my_gen = (i**2 for i in range(1,10))
print(list(my_gen))




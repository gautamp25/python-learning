import sys
some_word = ['voice','bark','apple',"convention",'crusade','perinnial']
# Normal function with list comprehension
def contains_i(words):
    return [word for word in words if "i" in word]
    
print(contains_i(some_word))
print(id(contains_i(some_word)))
print(sys.getsizeof((contains_i(some_word))))

# Generator function
"""
1. It's written like a regular function
2. Utilize the 'yield' keyword- A generator function contains the `yield` keyword so an internal state is kept and memory is saved.
3. yield keyword then return a lazy iterator- means contents are not stored in memory
4.  Generators can save you memory, making it easier to work with large data sets and other cumbersome tasks. 

-Interacting with Generator object
    1. convert type- can be converted into diff. types like List
    2. Loop- like other iterator can be also loop through 
    3. next()- to get greate control over accessing elements inside of generator object
    4. Generator objects are exhausted after the use.

    The yield statement produces a generator object and can return multiple values to the caller without terminating the program,
     whereas a return statement is used to return a value to the caller from within a function and it terminates the program.
       The return statement is used to return the value to the caller from within a function.
"""
def gen_contains_i(words):
    for word in words:
        if 'i' in word:
            yield word
print(list(gen_contains_i(some_word)))
print(id(list(gen_contains_i(some_word))))
print(sys.getsizeof(list(gen_contains_i(some_word))))
print("*"*20)

# convert type
gen_obj = gen_contains_i(some_word)
print(list(gen_obj))
print(set(gen_obj)) # empty set bcoz it exhausted
print(set(gen_contains_i(some_word)))
print(tuple(gen_obj))

# loop
print("***Loop****")
for el in gen_contains_i(some_word):
    print(el)

# next()
print("***Next****")
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))
# print(next(gen_obj))


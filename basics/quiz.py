def multiplier():
    return [lambda x:i*x for i in range(5)]
# a = multiplier()
# print(locals())
print([m(3) for m in multiplier()])

# print([lambda x=i:i*x for i in range(4)])

# b= [x*x for x in range(10)]
# print(b)
# c= [(lambda x: x*x)(x) for x in range(10)]
# print(c)
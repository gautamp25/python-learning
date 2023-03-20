# for i in range(1,13):
#     pass
#     print("sqr of {0:2} is {1:<3} and cube is {2}".format(i,i**2,i**3))

# parrot="Norwegian Blue"
# # print(parrot[1::2])

number = "9,333;789:890 78,653"
sep=""
for char in number:
    if not char.isnumeric():
        sep = sep+char

print(sep)

values = "".join(char if char not in sep else " " for char in number).split()
print([int(val) for val in values])
str1 = 'python'
str2 = 'Interpreter'
result = str1[:3]+str2[1:]
print(result)

# count = 0
def close():
    global count
    count = 0
    def inner():
        
        count+=1
        print(count)
    return inner

a = close()
a1 = close()
a()
a1()


def print_num(number):
    def printer():
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_num(9)
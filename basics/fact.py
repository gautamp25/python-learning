# recursive
def factorial(x):
    return 1 if x==1 or x==0 else x* factorial(x-1)

data = factorial(6)
print(data)

# iterative
def fact1(y):
    if y< 0:
        return 0
    elif y==0 or y==1:
        return 1
    else:
        fact=1
        while y>1:
            fact*=y
            y-=1
        return fact

d = print(fact1(6))
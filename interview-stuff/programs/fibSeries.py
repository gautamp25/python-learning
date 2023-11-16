# Fibonnaci series
# 1. Find the fibonnaci series from 0 to nth number using while loop

# 0 1 1 2 3 5 8 13 21 ....!

# By using while loop
def fibo(n):
    a,b = 0,1
    print(a)
    while(b<=n):
        print(b)
        a,b = b, a+b

fibo(7)

# Using for loop (n no.of terms)
print("Using for loop")
def fibo1(n):
    a,b = 0,1
    if n<=0:
        print("Not valid number")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            # print(a)
            c = a + b
            a = b
            b = c
            print(c)
            

fibo1(3)

# Using recursion
print("Using recursion")
def fibo3(n):
    if n<=1:
        return n
    else:       
        return fibo3(n-1) + fibo3(n-2) # (2-1)+(2-2)->1=2+1=3+2
n = 7
if n<=0:
    print("Not Valid number")
else:
    for i in range(n):
        print(fibo3(i))
    # print(i)
print("--------------")
def fibo4(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibo4(i-2)+fibo4(i-1)

print(fibo4(7))

for i in range(5):
    print(i)
cnt = 1
def fun1(a,b):
    global cnt
    if cnt<=5:
        cnt+=1
        return fun1(a+b,1)

res = fun1(1,2)
print(res)


    
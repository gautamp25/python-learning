def sqr(n):
    for i in range(1,n+1):
        yield i* i

        
a=sqr(3)
print(a)
print(next(a))
print(next(a))
print(next(a))
print("=============")

print(9/2)
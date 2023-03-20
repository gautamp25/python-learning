sqr = lambda x:x*x
print(sqr(5))

print((lambda y:y*y)(3))

l1 = [2,3,4,5]
d= [s*s for s in l1]
print(d)
p = {s:s*s for s in l1}
print(p)

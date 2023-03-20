l1= [1,2,3,4,5,6,7,8,9,10]
l2= ['a','b','c','d','e','f','g','h','i']
# l3= [a,b,c,d,e,f,g,h,i,j]

# o/p [1 a]
data = [f"{x}-{y}" for x in l1 for y in l2]
print(data)

# print(data)
# data = []
for x in l1:
    for y in l2:
        print(x,y)


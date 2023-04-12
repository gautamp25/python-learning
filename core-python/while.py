i=1
while i<=5:
    print(i)
    i+=1
print("While end")

j=0
while True:
    print(j)
    if j==3:
        break
    j+=1
print("While terminated")

a= 1
while a<=3:
    print("Outer loop",a)
    a+=1
    b=1
    while b<=5:
        print("Inner Loop",b)
        b+=1
print("END")

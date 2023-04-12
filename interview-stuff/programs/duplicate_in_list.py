# write program to find duplicate present in list
l = ['gtm',10,20,30,10,40,30,50,60]

duplicate_item = []
print(l.count(10))
for i in l:
    if l.count(i)>1 and i not in duplicate_item:
        duplicate_item.append(i)

print(duplicate_item)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] == l[j] and l[j] not in duplicate_item:
            duplicate_item.append(l[j])

print(duplicate_item)

str1= 'a3b2c4'
print(str1[0].isalpha())
op = ''
for i in range(len(str1)):
    if str1[i].isalpha():
        ch = str1[i]
    else:
        ch = ch*int(str1[i])
        op+=ch
print(op)

str2='aaabbcccc'
op = ''
count=1
for i in range(len(str2)-1):
    if str2[i]== str2[i+1]:
        count+=1
    else:
        op=op+str2[i]+str(count)
        count=1
op=op+str2[i]+str(count)
print(op)


str3 = "a,a,a,b,b,c,c,c,c"
my_list = str3.split(',')
print(my_list)
vis = []
for ch in my_list:
    if ch not in vis:
        print(f"{ch}:{my_list.count(ch)}",end=',')
        vis.append(ch)

# print(vis)

num = int(input("Enter number:"))
print(num)

def fact(n):
    if n<0:
        print("invalid")
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(-1))
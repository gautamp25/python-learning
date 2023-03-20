
age=25
height = 5.2
name =['Gtm','Harry','Peter']
myname = 'Harry'
class Dog:
    def __init__(self,name):
        self.name = name

    def get_details(self):
        print(f"My name is {myname} and age is- {age}")

obj = Dog('Harry')
obj.get_details()


st1 = {1, 2, 3}
st2 = {3, 4, 5}
print(st1 ^ st2)

a= 'Javascript'
def create():
    a='Solodity'
    print(a)

create()
print(a)

x=1
while x<=5:
    print(x)
    x+=1

for x in range(1,6):
    print(x)

print(False and True) # False
print(True and False) # False
print(True or True) # True
print(False and False) # False
print(True or False) # True
print(False or True) # True

if True or True:
    if False and True or False:
        print('a')
    elif False and False or True and True:
        print('b')
    else:
        print('c')
else:
    print('D')

A[5]

a = 3
b = 3
print(a**b)
print(a^b)

print(all([2,4,0,6])) # False- if any element zero then False else for non-zero returns True
print(5%5)

x = 1  
while True:  
    if x % 5 == 0:  
        break  
    print(x)   
    x += 1

m="gautam"
print(m[::-1])
print(m[1::])
print(m[::])
print(m[::3])
print(m[:-4])

print("Hello {0} and {1}".format(('foo', 'bin')))

str1="poWer"
str2="power"
print(id(str1))
print(id(str2))

dd=str1.upper()

print(str1)
print(dd)

str3="John,Simon,Aryan"
print(str3[-7:-12])
print(str3[-11:-7])
print(str3[-11:-6])
print(str3[-7:-11])

mydict={'a':1,'b':2}
print(mydict)
print(mydict.empty())

none="Hi"
print(None)
a = [[],[]]
b = [[]]*2
print(b)
a[0].append(10)
b[0].append(10)
print(a,b)

a = [1,'gautam']


list = ['G', 'A', 'U', 'T','A','M']
print(list[6:]) # Error []
print(list[-6:]) # ['G', 'A', 'U', 'T','A','M']
print(list[-7:]) # Error

def multipliers():
  return [lambda x : i * x for i in range(4)]
# print(multipliers())
print ([m(2) for m in multipliers()])
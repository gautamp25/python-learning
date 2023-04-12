"""
How kubernetes run on locally
What is kubernetes?
"""

def multipliers(x):
  return [lambda x : i * x for i in range(4)]
bb=multipliers(2)
for a in bb:
  print(a.next())
# print(list(bb))
# print ([m(2) for m in multipliers()])


class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x) # 1,1,1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x) # 1,2,1
Parent.x = 3
print (Parent.x, Child1.x, Child2.x) # 3,3,3

list = ['G', 'A', 'U', 'T','A','M']
print(list[6:]) # []
print (list[-6:]) # ['G', 'A', 'U', 'T','A','M']
print (list[-7:]) # ['G', 'A', 'U', 'T','A','M']



def multipliers():
  return [lambda x : i * x for i in range(4)]
    
print ([m(2) for m in multipliers()])
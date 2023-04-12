from re import A


my_tuple = (1,2,3,4)
my_dict = {}
my_dict[my_tuple] = "a"
print(my_dict)

def fib(n):
    a,b = 0,1
    while a<n:
        yield a
        a,b = b, a+b


x=fib(5)
print(x)


nums = [1,2,3,4,5]
print(nums[-1:-6:-2])
print(nums[0:6:2])

# Caret (^) operator
#It's a bitwise XOR (exclusive OR).
#It evaluates to True if and only if its arguments differ (one is True, the other is False).
x = 'b001'
y=[x.find('0')] #[1]
print(y)
z = len(y)^2
print(z)
print(5^2)
print(4^2) # 6(0110)
"""
0100
0010
-----
0110
"""


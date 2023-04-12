"""
1.difference in is operator and == operator
Ans= is operator ment for reference comparison or address comparison.
if two references are pointing to same objects then only is operator returns True.

== operator meant for content comparison,ie eventhough objects are different.
If content is same then == operator returns True

2. Explain Ternary Operator or Conditional Operator?
Ans: x = firstValue if condition else secondValue 

3. various built in Data types in python?
Ans- int, float,complex, string,boolean- fundamental
List,tuple,set,dictionary.

4. Mutable and Immutable?

5. Differnce in List & Tuple?
Ans: Detailed ans in diff_list_tuple.py


"""
l1 = [10,20,30]
l2 = [10,20,30]
print(l1 is l2) # False
print(l1==l2) # True

a = int(input("Enter first value:"))
b = int(input("Enter second value:"))

max = a if a>b else b
print("Max value is:",max)

for i in range(-5):
    print(i)

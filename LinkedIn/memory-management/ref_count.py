import sys
import gc
a= [1,2,3]
print(sys.getrefcount(a))

b = a
print(sys.getrefcount(b))

b = [1]
print(sys.getrefcount(b))

print(gc.get_threshold())

collected = gc.collect()
print(collected)
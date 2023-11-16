import time

lights = [
    ('green',2),
    ('yellow',0.5),
    ('red',2)
]
# i = 0
# while True:
#     c,s = lights[i]
#     print(c)
#     print(len(lights))
#     time.sleep(s)
#     if i==len(lights)-1:
#         i=0
#     else:
#         i+=1
from itertools import cycle
colors = cycle(lights)
print(colors)
while True:
    c,s = next(colors)
    print(c)
    time.sleep(s)
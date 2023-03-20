import numbers


# recursive depth
# O(log n)
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint+1:], target)
        else:
            return recursive_binary_search(list[:midpoint], target)

def verify(res):
    print("Target found:", res)

# number = [1,2,3,4,5,6,7,8,9,10]
number = [1,2,3]

result = recursive_binary_search(number, 4)
verify(result)

result = recursive_binary_search(number, 6)
verify(result)

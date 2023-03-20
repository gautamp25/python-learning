# Logarithmic Runtime
# O(log n)


def binary_search(list,target):
    first = 0
    last = len(list) - 1 # constant space
    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")

number = [1,2,3,4,5,6,7,8,9,10] #number list has to be sorted
result = binary_search(number, 12)
verify(result)

result = binary_search(number, 3)
verify(result)

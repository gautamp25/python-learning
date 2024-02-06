print("Hello world")
# stmt=1-1/3+1/5-1/7+1/9..1/49
# def test():
#     stm = ''
#     a=1

#     for i in range(1,20):
#         # stm =stm+ f"{a}-{a}/{+2}+"
#         stm = a+f"-
        
       
#     print(stm)
    
# test()

# sort arr
# arr = [4,3,1,5]
# def sort_fuc(arr):
#     a = 
#     for i in range(len(arr)):
#         if arr[i]> arr[i+1]:
#             arr[i]=arr[i+1]
#     print(arr)
    
# sort_fuc(arr)  

# table emp_id(1-5),name(a-e), mang_id(0-5)

# CREATE table employee(
#     id int,
#     emp_id int,
#     name varchar(50),
#     mang_id int

#     )
#     # mang of the emp
#     select * from emp where mang_id=1
#     isolation level,  merge stmt in sql
#     middleware in django clss and function base view
#     multilevel inheritance

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
my_array = [64, 34, 25, 12, 22, 11, 10]
bubble_sort(my_array)
print(my_array)
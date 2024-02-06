# Selection sort
# we need indexs in selection sort

"""
The function should perform the following tasks:

    Accept a parameter my_list that represents the list of integers to be sorted.

    Iterate through the list from the first element to the second-to-last element. For each element i, perform the following steps:

        Set min_index to the index of the current element i.

        Iterate through the list from the element at position i + 1 to the last element. For each element j, perform the following steps:

            Compare the element at position j with the element at position min_index. If the element at position j is less than the element at position min_index, update min_index to the index j.

        If the index i is not equal to min_index, swap the elements at positions i and min_index.

    Return the sorted list.

"""
my_list = [4,2,6,5,1,3]
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        # set min_index to i
        min_index = i 
        for j in range(i+1,len(my_list)):
            # compare j and min_index if j is less then set min_index equal j
            if my_list[j] < my_list[min_index]:
                min_index = j
            print(j)
        print('HI')
        if i!= min_index:
            print(i,j)
            # swap the values
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
            print("Swap",my_list)
    return my_list

print("Sorted list=",selection_sort(my_list))
nums =[2,15,11,7] 
target = 9
index_list = []
# def find_nums(nums,target):
# 	num_len = len(nums)
# 	for i in range(num_len-1):
#         for j in range(i+1,num_len):
#             if nums[i]+nums[j] == 9:
#                 index_list.append(i)
#                 index_list.append(i+1)

def find_nums(nums,target):
    index_list = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            print(i,j)
            print("sum",nums[i]+nums[j])
            if nums[i]+nums[j] == target:
                index_list.extend((i,j))
                print(index_list)
                return index_list

find_nums(nums,target)
# print(index_list)
    
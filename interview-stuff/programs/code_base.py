nums =[2,15,11,7] 
target = 9

# nums = [3,2,4]
# target = 6

def find_nums(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)): #(1,3)
            if nums[i]+nums[j] == target:
                return [i,j]

find_nums(nums,target)
# print(index_list)


def twoSum(nums, target):
    numToIndex = {}
    for i in range(len(nums)):
        if target - nums[i] in numToIndex:
            return [numToIndex[target - nums[i]], i]
        numToIndex[nums[i]] = i
    return []
print(twoSum(nums,target))


# Time complexity: O(N);
# Space Complexity: O(N);



nums = [2,11,15,7,4] #[0,1,2,3]
# nums = [3,2,4]
def sort_num(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            print(j)
            if nums[i]>nums[j]:
                nums[i],nums[j] = nums[j],nums[i] #3>2)(2,3)
    print(nums)
            
sort_num(nums)

    
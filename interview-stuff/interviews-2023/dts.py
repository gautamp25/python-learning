# 13-12-2023(6:15 PM- 6:30 PM)
# Decorators
# Lambda function
# Namespaces

# expecting exposure of numpy,pandas library

# nput: nums = [1,2,3,4,5,6,7], 
# If k = 3
# Output: [5,6,7,1,2,3,4]
# If k = 2
# Output: [6,7,1,2,3,4,5]
# If k = 1
# Output: [7,1,2,3,4,5,6]
nums = [1,2,3,4,5,6,7]
k=3
print(3%7)
print(nums[-3:])
print(nums[:-3])
def rotate_list(nums, k):
    k = k%len(nums)
    rotated_list = nums[-k:]+nums[:-k]
    return rotated_list 
print(rotate_list(nums,k))




# nput: s = " a good   example "
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string and also should not contain leading or trailing space
# s = " a good   example "
# d= ' '.join(s.split()[::-1])
# print(d)
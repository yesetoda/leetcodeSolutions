# from typing import List

# class Solution:
#     def createTargetArray( nums: List[int], index: List[int]) -> List[int]:
#         target = []
        
#         for num, idx in zip(nums, index):
#             target.insert(idx, num)
        
#         return target
#     print(createTargetArray(nums = [1], index = [0]))
nums = [5,5,5]
k = 2
nums.sort(reverse = True)
out = 0
for i in range(k):
    cur := nums[0]
    out+=cur
    # del nums[0]
    print(nums)
    nums.append(cur+1)
    nums.sort(reverse = True)
print(out)
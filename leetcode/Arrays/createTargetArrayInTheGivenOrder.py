# class Solution:
#     def createTargetArray(nums: list[int], index: list[int]) -> list[int]:
#         target = [0 for i in range(len(nums))]
#         for i in range(len(nums)):
#             print(i,index[i],nums[i])
#             target[index[i]] = nums[i]
#         return target
#     print(createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
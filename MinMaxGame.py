# def MMGame( nums: list[int]) -> int:
#         if len(nums) ==1:
#             return nums[0]
#         nw = []
#         even = True
#         for i in range(0,len(nums),2):
#             if even:
#                 nw.append(min(nums[i],nums[i+1]))
#                 even = False
#             elif not even:
#                 nw.append(max(nums[i],nums[i+1]))
#                 even  = True
#         return MMGame(nw)
# print(MMGame(nums = [1,3,5,2,4,8,2,2]))
from random import randint
print([randint(1, 10**9) for i in range(1024)])
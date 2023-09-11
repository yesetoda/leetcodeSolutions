from random import randint
# class Solution:
#     def longestConsecutive( nums: list[int]) -> int:
#         srt = sorted(nums)
#         out = 1
#         mx = 0
#         for i in range(1,len(nums)):
#             if srt[i]-srt[i-1]==1:
#                 mx+=1
#                 if mx>out:
#                     out=mx
#         return out
print([randint(1,1000) for i in range(10**4)])
class Solution:
    def minOperations(nums: list[int]) -> int:
        op = 0
        for i in range(1,len(nums)):
            while nums[i-1]>=nums[i]:
                op+=nums[i-1]-nums[i]+1
                nums[i] = nums[i]+(nums[i-1]-nums[i]+1)
        return op
    print(minOperations(nums = [1]))
from random import randint
print([randint(1,10000) for i in range(5000)])
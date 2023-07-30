class Solution:
    def numIdenticalPairs( nums: list[int]) -> int: 
        out = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    out+=1
        return out
    print(numIdenticalPairs( nums = [1,2,3]))

 
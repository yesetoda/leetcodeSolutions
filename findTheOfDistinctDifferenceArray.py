class Solution:
    def distinctDifferenceArray( nums: list[int]) -> list[int]:
        return [ (len(set(nums[:i+1]))-len(set(nums[i+1:])))  for i in range(len(nums))]
    print(distinctDifferenceArray(nums = [3,2,3,4,2]))
class Solution:
    def buildArray( nums: list[int]) -> list[int]:
        out = []
        for i in nums:
            out.append(nums[i])
        return out
    print(buildArray( nums = [5,0,1,2,3,4]))
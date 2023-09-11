class Solution:
    def maximumDifference( nums: list[int]) -> int:
        mx= -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    val = nums[j]-nums[i]
                    if mx<val:
                        mx = val
        return mx
    print(maximumDifference(nums = [1,5,2,10]))
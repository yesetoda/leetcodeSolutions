class Solution:
    def intersection1(nums: list[list[int]]) -> list[int]:
        out  = set(nums[0])
        for i in nums:
            out = out.intersection(set(i))
        return sorted(out)
    print(intersection1( nums = [[1,2,3],[4,5,6]]))
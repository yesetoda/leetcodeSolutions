class Solution:
    def specialArray( nums: list[int]) -> int:
        nums = sorted(nums)
        x = len(nums)
        for i in nums:
            if x<=i:
                return x
            else:
                x-=1
        return -1
    print(specialArray( [3,5]))
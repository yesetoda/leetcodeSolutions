class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        maxnum = max(nums)
        minnum = min(nums)
        new_list = [num for num in nums if num not in [maxnum, minnum]]
        if len(new_list) == 0:
            return -1
        else:
            return new_list[0]
    print(findNonMinOrMax( nums = [2,1,3]))
class Solution:
    def rangeSum( nums: list[int], n: int, left: int, right: int) -> int:
        out = []
        for i in range(len(nums)-1):
            sm = nums[i]
            out.append(sm)
            for j in range(i+1,len(nums)):
                sm+=nums[j]
                out.append(sm)
        for i in set(nums):
            if i not in set(out):
                out.append(i)
        out.sort()
        return sum(out[left-1:right])
    print(rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5))


        
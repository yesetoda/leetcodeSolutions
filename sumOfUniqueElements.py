class Solution:
    def sumOfUnique( nums: list[int]) -> int:
        out = 0
        for i in set(nums):
            if nums.count(i)==1:
                out+=i
        return out
    print(sumOfUnique(nums = [1,2,1,3,2]))
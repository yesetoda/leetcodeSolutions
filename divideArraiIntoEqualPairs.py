class Solution:
    def divideArray( nums: list[int]) -> bool:
        for i in set(nums):
            if nums.count(i)%2==1:
                return False
        return True
    print(divideArray(nums = [1,2,3,4]))
class Solution:
    def sumOfSquares(nums: list[int]) -> int:
        out= 0
        for i in range(1,len(nums)+1):
            if len(nums)%i ==0:
                out+= nums[i-1]**2
        return out
    print(sumOfSquares( nums = [1,2,3,4]))
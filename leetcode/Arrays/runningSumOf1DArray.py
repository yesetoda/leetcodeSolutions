class Solution:
    def runningSum(nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            if i==0:
                pass
            else:
                nums[i] = nums[i] + nums[i-1]
        return nums
    nums = [3,1,2,10,1]
    print(runningSum(nums))
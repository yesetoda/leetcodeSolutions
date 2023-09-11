class Solution:
    def maxOperations(nums: list[int], k: int) -> int:
        cnt = 0
        st = 0
        end = len(nums)-1
        while st!=end:
            if nums[st]+nums[end]==k:
                nums.remove(nums[st])
                nums.remove(nums[end])
                cnt+=1
                st = 0
                end = len(nums)-1
            elif nums[st]+nums[end]>k:
                end-=1
            elif nums[st]+nums[end]<k:
                st+=1
        return cnt
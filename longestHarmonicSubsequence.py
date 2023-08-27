class Solution:
    def findLHS(nums: list[int]) -> int:
        nums.sort()
        mx = 0
        # end = len(nums)
        for i in range(len(nums)-1):
            st  =i
            end = len(nums)-1
            print(st,end,nums[st],nums[end],abs(nums[st] -nums[end]))
            while end!=st and abs(nums[st] -nums[end]) !=1:
                print("while==>",st,end,nums[st],nums[end],abs(nums[st] -nums[end]),mx)
                end-=1
            if mx<abs(st-end):
                    mx=abs(st-end)
        return mx
    print(findLHS(nums = [1,3,2,2,5,2,3,7]))
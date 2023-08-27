class Solution:
    def productExceptSelf( nums: list[int]) -> list[int]:
        out = []
        for i in range(len(nums)):
            if i==0:
                out.append(nums[i+1:])
            else:
                out.append(nums[:i]+nums[i+1:])
        print(out)
        
        for i in out:
            result = 1
            for
            
    print(productExceptSelf(nums = [1,2,3,4]))
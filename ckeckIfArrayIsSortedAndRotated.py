class Solution:
    def check( nums: list[int]) -> bool:
        out = sorted(nums)
        mn = nums[0]
        if nums == out:
            return True
        for i in nums:
            if i>=mn:
                mn = i
                out.insert(0,out.pop())
            else:
                break
        return nums == out
    print( check(nums = [3,4,5,1,2] ))
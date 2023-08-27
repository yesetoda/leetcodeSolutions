class Solution:
    def distinctAverages(nums: list[int]) -> int:
        nums = sorted(nums)
        s = set()
        while nums:
            print(nums)
            s.add((nums[0]+nums.pop())/2)
            nums = nums[1:]
        return len(s)
    print(distinctAverages(nums = [1,1,100,100]))
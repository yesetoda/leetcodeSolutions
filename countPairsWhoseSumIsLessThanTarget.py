class Solution:
    def countPairs( nums: list[int], target: int) -> int:
        nums = sorted(nums)
        count = 0
        leng  = len(nums)
        for i in range(leng-1):
            for j in range(i+1,leng):
                if nums[i]+nums[j]>=target:
                    break
                elif nums[i]+nums[j] < target:
                    count+=1
        return count
    print(countPairs( nums = [-6,2,5,-2,-7,-1,3], target = -2))
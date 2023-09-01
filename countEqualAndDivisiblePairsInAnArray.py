class Solution:
    def countPairs( nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1
        return count
    print(countPairs(nums = [1,2,3,4], k = 1))
        
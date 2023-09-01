from itertools import combinations

class Solution:
    def minimumDifference( nums: list[int], k: int) -> int:
        if len(nums)<2:
            return 0
        mn = (10**5)+1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])<mn:
                    mn = abs(nums[i]-nums[j])
        return mn
    print(minimumDifference([1,2,3,2,4,2,6,76,45,3,3,2,53,43,7],9))
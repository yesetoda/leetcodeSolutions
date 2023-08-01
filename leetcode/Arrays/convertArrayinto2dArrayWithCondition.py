from collections import Counter
class Solution:
    def findMatrix( nums: list[int]) -> list[list[int]]:
        
        rows = max(Counter(nums).values())
        l = [[] for i in range(rows)]
        for i in range(len(nums)):
            for j in range(rows):
                if nums[i] not in l[j]:
                    l[j].append(nums[i])
                    break
        return l
    print(findMatrix(nums = [1,2,3,4,1,1,1,3,32,5,543,53]))
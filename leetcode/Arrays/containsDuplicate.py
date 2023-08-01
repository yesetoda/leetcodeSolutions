from collections import Counter
class Solution:
    def containsDuplicate(nums: list[int]) -> bool:
        numset = set(nums)
        return len(numset)!=len(nums)
    print(containsDuplicate( nums = [1,1,1,3,3,4,3,2,4,2]))
from time import perf_counter
from random import randint
class Solution:
    def arrayPairSum(nums: list[int]) -> int:
        print(nums)
        sm = 0
        nums = sorted(nums)
        for ind in range(0,len(nums),2):
                sm+=nums[ind]
        return sm
    a = perf_counter()
    print(arrayPairSum([randint(-10**3,10**4) for i in range(10**4)]))
    b = perf_counter()
    print(b-a)
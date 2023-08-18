from time import perf_counter
class Solution:
    def maximumCount( nums: list[int]) -> int:
        p = 0
        n = 0
        for i in nums:
            if i>0:
                p+=1
            if i<0:
                n+=1
        # print(p,n)
        return max(p,n)
    a = perf_counter()
    print(maximumCount(nums = [5,20,66,1314]))
    c = perf_counter()
    print(c-a)
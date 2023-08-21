from time import perf_counter
class Solution:
    def findLucky( arr: list[int]) -> int:
        x = list(set(arr))[::-1]
        # print(x)
        for i in x:
            if i == arr.count(i):
                return i
        return -1
    t1 = perf_counter()
    print(findLucky(arr = [i%100 for i in range(10**4)])) 
    t2 = perf_counter()
    print(t2-t1)
        
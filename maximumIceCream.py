from random import randint
class Solution:
    def maxIceCream(costs: list[int], coins: int) -> int:
        costs.sort()
        iceCreams = 0
        for i in costs:
            if coins-i>=0:
                coins-=i
                iceCreams+=1
            else:
                return iceCreams
        return len(costs)
    print([randint(1,10**5) for i in range(10**4)])
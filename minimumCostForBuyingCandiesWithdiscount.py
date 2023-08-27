class Solution:
    def minimumCost(cost: list[int]) -> int:
        s  = sorted(cost)
        pay = 0
        for i in range(len(cost)):
            if i%3!=len(cost)%3:
                pay+=s[i]
        return pay
    def w(cost: list[int]):
        cost.sort()
        res = 0
        for i in range(len(cost)):
            if i%3 != len(cost)%3: res+=cost[i]
        return res

    print(minimumCost(cost = [5 for i in range(100)]))
    print(w(cost = [5 for i in range(100)]))
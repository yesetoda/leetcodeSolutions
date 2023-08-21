class Solution:
    def maxCoins( piles: list[int]) -> int:
        piles = sorted(piles,reverse=True)
        print(piles)
        out = 0
        for i in range(0,len(piles)//3*2,2):
            out+=piles[i+1]
        return out
    print(maxCoins(piles = [1,-2,3]))
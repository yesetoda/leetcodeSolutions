class Solution:
    def distributeCandies(candyType: list[int]) -> int:
        return len(set(candyType)) if len(set(candyType))<=len(candyType)//2 else len(candyType)//2
    print(distributeCandies(candyType = [-i for i in range(10**4)]))
        
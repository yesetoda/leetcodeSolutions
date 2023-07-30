class Solution:
    def kidsWithCandies( candies: list[int], extraCandies: int) -> list[bool]:
        greatest = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                candies[i] = True
            else:
                candies[i] = False
        return candies
    print(kidsWithCandies(candies = [12,1,12], extraCandies = 10))
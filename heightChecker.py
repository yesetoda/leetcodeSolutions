class Solution:
    def heightChecker( heights: list[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if expected[i]!=heights[i]:
                count+=1
        return count
    print(heightChecker(heights = [1,2,3,4,5]))
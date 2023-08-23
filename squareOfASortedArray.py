class Solution:
    def sortedSquares(nums: list[int]) -> list[int]:
        return sorted([i**2 for i in nums])
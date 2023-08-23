class Solution:
    def findFinalValue(nums: list[int], original: int) -> int:
        s = set(nums)
        while original in s:
            original*=2
        return original
class Solution:
    def maxProduct( nums: list[int]) -> int:
        srt = sorted(nums)
        return (srt[-1]-1)*(srt[-2]-1)
    print(maxProduct(nums = [1,5,4,5]))
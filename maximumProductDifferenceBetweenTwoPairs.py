class Solution:
    def maxProductDifference(nums: list[int]) -> int:
        srt = sorted(nums)
        return srt[-1]*srt[-2]-srt[0]*srt[1]
    print(maxProductDifference(nums = [4,2,5,9,7,4,8]))
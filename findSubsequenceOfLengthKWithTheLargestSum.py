class Solution:
    def maxSubsequence( nums: list[int], k: int) -> list[int]:
        # srt = sorted(nums,reverse = True)[:k]
        # srt.sort(key = lambda x:nums.index(x))
        #  return srt
        sorted_nums = sorted(nums, reverse=True)
        max_subsequence = sorted_nums[:k]
        max_subsequence.sort()
        return max_subsequence
    print(maxSubsequence( nums = [18,3,19,-8,30,22,-35,11,16,18,-21,32,-7,-6,38,25,-21,-1,26,-8,-37,-39,-34,6,-36,-3,26,-32,22,-20,35,-35,-30,-8,11,7,-23,-9,-22,1,33,-6,12,2,27,-27,28,-12,21,12,16,21,33], k =
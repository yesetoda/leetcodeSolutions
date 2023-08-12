from collections import Counter
class Solution:
    def frequencySort( nums: list[int]) -> list[int]:
        freq = Counter(nums)
        print(freq)
        out = ""
        for i,j in  freq.items():
            
    print(frequencySort(nums = [1,1,2,2,2,3]))
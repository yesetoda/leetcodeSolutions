from collections import Counter
class Solution:
    def numberOfPairs( nums: list[int]) -> list[int]:
        freq = Counter(nums)
        lefts = 0
        pairs = 0
        for i in freq.keys():
            if freq[i]%2 ==0:
                pairs+=freq[i]/2
            else:
                x = freq[i]-1
                lefts+=1
                pairs+=x/2
        return [int(pairs),lefts]
    print(numberOfPairs(nums = [0]))
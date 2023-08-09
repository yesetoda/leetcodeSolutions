from collections import Counter
class Solution:
    def topKFrequent(nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        return [x for x, _ in freq.most_common(k)]
    print(topKFrequent( nums = [3,0,1,0], k = 1))
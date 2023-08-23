from collections import Counter
class Solution:
    def mostFrequentEven(nums: list[int]) -> int:
        freq = Counter(sorted(nums)).most_common()
        for i in freq:
            if i[0]%2 == 0:
                return i[0]
        return -1
    print(mostFrequentEven(nums = [29,47,21,41,13,37,25,7]))
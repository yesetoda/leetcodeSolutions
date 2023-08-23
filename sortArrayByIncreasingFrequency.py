from collections import Counter
class Solution:
    def frequencySort( nums: list[int]) -> list[int]:
        out  = []
        for i in Counter(sorted(nums)).most_common():
            for j in range(i[1]):
                out.append(i[0])
        return out[::-1]
    print(frequencySort(nums = [1,5,0,5]))
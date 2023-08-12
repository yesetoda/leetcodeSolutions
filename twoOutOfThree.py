from collections import Counter
class Solution:
    def twoOutOfThree( nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        l = list(set(nums1))
        l.extend(list(set(nums2)))
        l.extend(list(set(nums3)))
        freq = Counter(l)
        out = [i for i in list(freq.keys()) if freq[i]>=2]
        return set(out)
    nums1 = [i for i in range(1,101)]
    print(twoOutOfThree( nums1 , nums2 = [2,3], nums3 = [1,3]))
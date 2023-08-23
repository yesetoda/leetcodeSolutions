from collections import Counter
from random import randint
class Solution:
    def majorityElement( nums: list[int]) -> list[int]:
        leng = len(nums)
        if leng<3:
            return senums
        out = []
        freq = Counter(nums).most_common()
        requirement = leng/3
        if freq[0][1]<=requirement:
            return []
        else:
            for num,count in freq:
                if count>requirement:
                    out.append(num)
        return out
    print(majorityElement(nums = [randint(1, 4) for i in range(5 * 10**4)]))
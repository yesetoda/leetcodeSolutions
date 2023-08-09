from collections import Counter
class Solution:
    def majorityElement( nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
    print(majorityElement( nums = [3,3,3,2,3]))
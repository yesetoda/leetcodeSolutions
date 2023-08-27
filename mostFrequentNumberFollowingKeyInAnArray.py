from collections import Counter
class Solution:
    def mostFrequent( nums: list[int], key: int) -> int:
        out = []
        for i in range(nums.count(key)):
            ind = nums.index(key)
            if ind<len(nums)-1:
                nums = nums[ind+1:]
                print(ind,nums)
                out.append(nums[0])
        # print(out,Counter(out))
        return Counter(out).most_common()[0][0]
    print(mostFrequent(nums = [2,2,2,2,3], key = 2))
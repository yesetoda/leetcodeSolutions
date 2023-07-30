class Solution:
    def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
        out = []
        for i in nums:
            count = 0
            for j in nums[::]:
                if i > j:
                    count+=1
            out.append(count)
        return out
    print(smallerNumbersThanCurrent(nums = [7,7,7,7]))
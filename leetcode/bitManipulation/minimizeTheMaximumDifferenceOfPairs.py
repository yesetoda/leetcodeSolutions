def possiblePairs(nums, p, max_diff):
        count = 0
        i = 0
        j = 0

        while i < len(nums) and count <= p:
            while j < len(nums) and nums[j] - nums[i] <= max_diff:
                j += 1
            count += j - i - 1
            i += 1

        return count >= p
class Solution:
    def minimizeMax(nums: list[int], p: int) -> int:
        # out = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         out.append(abs(nums[i]-nums[j]))
        # printable = []
        # print(out)
        # for i in range(p):
        #     printable.append(min(out))
        #     del out[out.index(min(out))]
        # print(printable)
        # if p == 0:
        #     return 0
        # else:return max(printable)
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        low = 0
        high = nums[-1] - nums[0]  # Maximum possible difference

        while low < high:
            mid = (low + high) // 2
            if possiblePairs(nums, p, mid):
                high = mid
            else:
                low = mid + 1

        return low
    print(minimizeMax([3,4,2,3,2,1,2],3))

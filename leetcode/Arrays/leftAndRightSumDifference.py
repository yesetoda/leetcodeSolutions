class Solution:
    def leftRightDifference( nums: list[int]) -> list[int]:
        totalsum = sum(nums)
        ls = []
        rs  = []
        out = []
        ls.append(0)
        rs.append(totalsum -nums[0])
        for i in range(len(nums)):
            if i==len(nums)-1:
                pass
            else:
                ls.append(ls[i]+nums[i])
                rs.append(rs[i]-nums[i+1])
        for i in range(len(nums)):
            out.append(abs(rs[i]-ls[i]))
        return out
    print(leftRightDifference( nums = [10,4,8,3]))
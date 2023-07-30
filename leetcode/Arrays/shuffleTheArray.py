class Solution:
    def shuffle( nums: list[int], n: int) -> list[int]:
        out = []
        for  i in range(n):
            out.append(nums[:n][i])
            out.append(nums[n:][i])
        return out
    print(shuffle(nums = [1,1,2,2], n = 2))
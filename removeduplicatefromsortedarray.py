class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        out = []
        for i in nums:
            if i in out:
                pass
            else:
                out.append(i)
        return len(out)
    print(removeDuplicates(nums = [1,1,2]))
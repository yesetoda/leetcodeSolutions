class Solution:
    
    def minimumOperations(nums: list[int]) -> int:
        out = []
        for i in nums:
            if i>0:
                out.append(i)
        return len(set(out))
    nums = [0]
    print(minimumOperations(nums))
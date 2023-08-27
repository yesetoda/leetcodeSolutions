class Solution:
    def findTheArrayConcVal(nums: list[int]) -> int:
        conVal = 0
        while len(nums)>=2:
            conVal+=int(str(nums[0])+str(nums[-1]))
            nums = nums[1:]
            nums.pop()
        if nums:
            conVal+=nums[0]
        return conVal
    print(findTheArrayConcVal( nums = [5,14,13,8,12]))
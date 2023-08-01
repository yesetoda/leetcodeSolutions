class Solution:
    def separateDigits(nums: list[int]) -> list[int]:
        numstr = [str(i) for i in nums]
        numstr = "".join(numstr)
        return [int(i) for i in numstr]
        
    print(separateDigits(nums = [7,1,3,9]))

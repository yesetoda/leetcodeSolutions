class Solution:
    def getConcatenation( nums: list[int]) -> list[int]:
        nums+=nums
        return nums
    nums = [1,2,1]
    print(getConcatenation(nums))
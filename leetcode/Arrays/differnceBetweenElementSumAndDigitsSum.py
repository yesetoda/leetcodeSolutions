class Solution:
    def differenceOfSum( nums: list[int]) -> int:
        digitstr = "".join(str(nums)).replace(",","").replace("[","").replace("]","").replace(" ","")
        elementSum = sum(nums)
        digitSum  = 0
        for i in digitstr:
            digitSum+=int(i)
        return abs(elementSum-digitSum)
    print(differenceOfSum(nums = [1,2,3,4]))
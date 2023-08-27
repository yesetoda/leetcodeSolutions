class Solution:
    def sortEvenOdd( nums: list[int]) -> list[int]:
        oddInd = []
        evenInd = []
        out = []
        for i in range(len(nums)):
            if i%2 == 0:
                evenInd.append(nums[i])
            else:
                oddInd.append(nums[i])
        oddInd = sorted(oddInd , reverse = True)
        evenInd = sorted(evenInd)
        for i in range(len(nums)):
            if i%2 == 0:
                out.append(evenInd[i//2])
            else:
                out.append(oddInd[(i-1)//2])
        return out
    print(sortEvenOdd(nums = [2,1]))
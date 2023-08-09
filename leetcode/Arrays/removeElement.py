class Solution:
    def removeElement( nums: list[int], val: int) -> int:
        out = []
        count = 0
        for i in nums:
            if i!=val:
                out.append(i)
                count+=1
        lnums = len(nums)
        lout = len(out[::])
        for i in range(lnums-lout):
            out.append("_") 
        return str(count)+", "+str(out)
    print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
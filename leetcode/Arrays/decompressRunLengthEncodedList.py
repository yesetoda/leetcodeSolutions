class Solution:
    def decompressRLElist( nums: list[int]) -> list[int]:
        s=""
        out = []
        for i in range(len(nums)):
            if i%2 == 0:
                s+= (str(nums[i+1])+ " ")*nums[i]
        for i in s.split():
            print(i)
            out.append(int(i))
        return out
    print(decompressRLElist(nums = [1,1,2,3]))
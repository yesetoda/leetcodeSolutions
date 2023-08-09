class Solution:
    def sumOddLengthSubarrays(arr: list[int]) -> int:
        out = 0
        for i in range(0,len(arr),2):
            for j in range(len(arr)):
                if j+i+1<=len(arr):
                    out+=sum(arr[j:j+i+1])
                else:
                    break
        return out
    print(sumOddLengthSubarrays(arr = [10,11,12]))
        
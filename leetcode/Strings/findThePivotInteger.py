class Solution:
    def pivotInteger(n: int) -> int:
        out = [i for i in range(1,n+1)]
        for i in range(n,0,-1):
            if sum(out[i-1:]) == sum(out[:i]):
                return i
        return -1
    print(pivotInteger(n = 8))
        
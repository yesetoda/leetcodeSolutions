class Solution:
    def kthFactor( n: int, k: int) -> int:
        out = []
        for i in range(1,n+1):
            if n%i==0:
                out.append(i)
            # print(out)
            if len(out)==k:
                return out[-1]
        return -1
    print(kthFactor(n = 700000, k = 72))
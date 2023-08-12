class Solution:
    def combine( n: int, k: int) -> list[list[int]]:
        out = []
        if n==1 and k==1:
            return [[1]]
        for j in range(1,2*k+1):
            for i in range(k,n+1):
                if i != j and i>j:
                    out.append([j,i])
        return out
    print(combine(3,1))
class Solution:
    def distinctIntegers( n: int) -> int:
        dist = [n,n-1]
        x = dist[1]
        while x>=1:
            if x%2==0:
                x//=2
                dist.append(x)
            else:
                x-=x
                if x>0:
                    dist.append(x)
        return len(dist)
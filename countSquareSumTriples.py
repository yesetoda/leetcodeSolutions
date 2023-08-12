class Solution:
    def countTriples(n: int) -> int:
        count=0
        perfectSquare = [i**2 for i in range(1,n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i**2+j**2 in perfectSquare:
                    count+=1
        return count
    print(countTriples(5))
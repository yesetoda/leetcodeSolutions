class Solution:
    def smallestEvenMultiple( n: int) -> int:
        out=  2
        while(True):
            if out%n ==0 and out%2==0:
                return out
            else:
                out+=2
    print(smallestEvenMultiple( n =6))
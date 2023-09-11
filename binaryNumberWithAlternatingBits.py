class Solution:
    def hasAlternatingBits(n: int) -> bool:
        print(print(n),bin(n)[2:])
        bnr = bin(n)[2:]
        for i in range(1,len(bnr)):
            if bnr[i-1]==bnr[i]:
                return False
        return True
    print(hasAlternatingBits(2**31 -1))
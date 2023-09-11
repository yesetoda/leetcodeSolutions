class Solution:
    def binaryGap( n: int) -> int:
        bnr = bin(n)[2:]
        cnt = bnr.count("1")
        mx = 0
        if cnt<2:
            return 0
        else:
            ind = 0
            for _ in range(cnt-1):
                ind1 = bnr.index("1")
                bnr = bnr[:ind1]+"0"+bnr[ind1+1:]
                ind2 = bnr.index("1")
                if mx<ind2-ind1:
                    mx = ind2-ind1
        return mx
    print(binaryGap(5))
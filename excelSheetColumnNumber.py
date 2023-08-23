class Solution:
    def titleToNumber( columnTitle: str) -> int:
        l = {chr(64+i):i for i in range(1,27)}
        ind = 0
        out = 0
        for i in columnTitle[::-1]:
            out +=l[i]*26**ind
            ind+=1
        return out
    print(titleToNumber("XYZ"))
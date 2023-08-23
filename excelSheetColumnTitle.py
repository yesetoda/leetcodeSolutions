class Solution:
    def convertToTitle( columnNumber: int) -> str:
        l = {i:chr(64+i) for i in range(1,27)}
        out = ""
        i =columnNumber
        while columnNumber>0:
            remain = (columnNumber-1)%26 
            out = l[remain+1]+out
            columnNumber = (columnNumber-1)//26
        return out
    print(convertToTitle(127))
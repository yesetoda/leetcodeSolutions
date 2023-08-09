class Solution:
    def cellsInRange(s: str) -> list[str]:
        l = s.split(":")
        startcol = ord(l[0][0])
        startNum = int(l[0][1])
        r1 = ord(l[1][0])-startcol
        r2 = int(l[1][1])-startNum
        print(r1,r2)
        out = []
        for i in range(r1+1):
            for j in range(r2+1):
                out.append(chr(startcol+i)+str(startNum+j))
        return out
    print(cellsInRange(s = "U7:X9"))
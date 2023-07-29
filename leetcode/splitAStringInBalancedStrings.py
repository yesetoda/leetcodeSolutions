class Solution:
    def balancedStringSplit( s: str) -> int:
        numR = 0
        numL = 0
        out = 0
        for i in s:
            if i == "R":
                numR+=1
            if i == "L":
                numL+=1
            if numL == numR and (numL!=0 and +numR !=0):
                out+=1
            print(i,numL,numR,out)
        return out
    s = "LLLLRRRR"
    print(balancedStringSplit(s))
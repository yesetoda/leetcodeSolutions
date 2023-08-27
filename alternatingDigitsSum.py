class Solution:
    def alternateDigitSum(self, n: int) -> int:
        out = 0
        for ind,ch in enumerate(str(n)):
            if ind%2 == 0:
                out+=int(ch)
            else:
                out-=int(ch)
        return out
    print(alternateDigitSum())
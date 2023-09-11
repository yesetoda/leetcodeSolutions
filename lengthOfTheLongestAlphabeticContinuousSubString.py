class Solution:
    def longestContinuousSubstring(s: str) -> int:
        out = 0
        mx = 1
        for i in range(1,len(s)):
            if ord(s[i])-ord(s[i-1])==1:
                mx+=1
                if mx>out:
                    out = mx
            else:
                mx =0
        return out
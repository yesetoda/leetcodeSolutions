class Solution:
    def shortestToChar( s: str, c: str) -> list[int]:
        # out = []
        # for i in range(len(s)):
        #     print(i,s[:i+1].index(c),s[i:].index(c),min((s[0:i+1].index(c)),(s[i:].index(c))))
        #     out.append(min((s[:i+1].index(c)),(s[i:].index(c))))
        # return out
        out = []
        prev = float('-inf')
        
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            out.append(i - prev)
            
        prev = float('inf')
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            out[i] = min(out[i], prev - i)
            
        return out
    print(shortestToChar( s = "loveleetcode", c = "e"))
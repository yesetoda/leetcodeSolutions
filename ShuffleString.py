class Solution:
    def restoreString( s: str, indices: list[int]) -> str:
        out = [0 for i in range(len(s))]
        for i in range(len(s)):
            out[indices[i]]=s[i]
        return "".join(out)
    print(restoreString( s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
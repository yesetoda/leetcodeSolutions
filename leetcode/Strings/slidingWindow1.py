class Solution:
    def countGoodSubstrings(s: str) -> int:
        out = []
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == len(s[i:i+3]):
                out.append(s[i:i+3])
        return len(out)


solution = Solution()
print(solution.countGoodSubstrings(s="xyzzaz"))
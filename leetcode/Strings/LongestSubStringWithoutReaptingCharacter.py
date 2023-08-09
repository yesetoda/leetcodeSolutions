class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        max_length = 0
        start = 0
        seen = {}

        for end in range(len(s)):
            if s[end] in seen and start <= seen[s[end]]:
                start = seen[s[end]] + 1
            else:
                max_length = max(max_length, end - start + 1)
            seen[s[end]] = end

        return max_length
print(Solution.lengthOfLongestSubstring(s="dvdf"))
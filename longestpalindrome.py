from collections import Counter
class Solution:
    def longestPalindrome( s: str) -> int:
        freq = Counter(s)
        odd_count = 0
        out = 0

        for fr in freq.values():
            if fr % 2 == 1:
                odd_count += 1
                out += fr - 1
            else:
                out += fr

        if odd_count > 0:
            out += 1

        return out
    print(longestPalindrome(s = "abccccdd"))
# class Solution:
#     def longestPalindrome( s: str) -> str:
#         start = 0
#         end=len(s)-1
#         out = ""
#         while True:
#             if start == end:
#                 out+=s[start]
#                 print(out)
#                 break
#             elif s[start] != s[end]:
#                 end-=1
#                 print(out)
#             elif s[start] == s[end]:
#                 start+=1
#                 end-=1
#             print(out)
        # return out
class Solution:
    def longestPalindrome(s):
            n = len(s)
            dp = [[False] * n for _ in range(n)]
            start = 0
            maxLength = 0

            for i in range(n - 1, -1, -1):
                for j in range(i, n):
                    if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                        dp[i][j] = True
                        if j - i + 1 > maxLength:
                            maxLength = j - i + 1
                            start = i

            return s[start:start + maxLength]
    longestPalindrome(s = "aba") 
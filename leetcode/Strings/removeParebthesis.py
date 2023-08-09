class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        for i in range(len(s)):
            if s[i]=="(" and s[i+1]=="(":
                storeOpen = i
            elif s[i]==")":
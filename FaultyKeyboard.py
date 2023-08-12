class Solution:
    def finalString(s: str) -> str:
        prev = ""
        for i in range(len(s)):
            if s[i] == "i":
                prev = prev[::-1]
            else:
                prev+=s[i]
        return prev
    print(finalString("poiinter"))
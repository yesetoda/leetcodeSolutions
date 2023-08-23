class Solution:
    def firstPalindrome( words: list[str]) -> str:
        def ispali(s):
            for i in range(len(s)//2):
                if s[i] != s[-1-i]:
                    return False
            return True
        for i in words:
            if ispali(i):
                return i
        return ""
    print(firstPalindrome(words = ["def","ghi"]))
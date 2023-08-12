class Solution:
    def reverseOnlyLetters( s: str) -> str:
        letters = [i for i in s if i.isalpha()][::-1]
        for ind,ch in enumerate(s):
            if not ch.isalpha():
                letters.insert(ind,ch)
        return "".join(letters)
    print(reverseOnlyLetters(s = "Test1ng-Leet=code-Q!"))
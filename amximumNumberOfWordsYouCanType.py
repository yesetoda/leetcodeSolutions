class Solution:
    def canBeTypedWords(text: str, brokenLetters: str) -> int:
        # brokenLetters = [i for i in brokenLetters]
        count = len(text.split())
        for i in text.split():
            if any(letter in i for letter in brokenLetters):
                count-=1
        return count
    print(canBeTypedWords(text = "leet code", brokenLetters = "e"))
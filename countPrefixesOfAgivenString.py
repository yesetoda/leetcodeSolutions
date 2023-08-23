class Solution:
    def countPrefixes( words: list[str], s: str) -> int:
        count  = 0
        for i in set(words):
            if s.startswith(i):
                count+=words.count(i)
        return count
    print(countPrefixes( words = ["a","a"], s = "aa"))
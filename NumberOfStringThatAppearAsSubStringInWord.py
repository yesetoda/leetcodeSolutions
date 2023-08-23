class Solution:
    def numOfStrings(patterns: list[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count+=1
        return count
    print(numOfStrings( patterns = ["a","a","a"], word = "ab"))
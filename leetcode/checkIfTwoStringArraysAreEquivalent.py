class Solution:
    def arrayStringsAreEqual( word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)
    word1  = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(arrayStringsAreEqual(word1,word2))
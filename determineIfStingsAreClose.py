class Solution:
    def closeStrings( word1: str, word2: str) -> bool:
        a = sorted([word1.count(i) for i in word1])
        b = sorted([word2.count(i) for i in word2])
        return a==b
    print(closeStrings( word1 = "cabbba", word2 = "abbccc" ))
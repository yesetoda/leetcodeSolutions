from collections import Counter
class Solution:
    def areOccurrencesEqual( s: str) -> bool:
        freq = len(set(Counter(s).values()))
        return freq==1
    print(areOccurrencesEqual("aaabb"))
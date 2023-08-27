from collections import Counter
class Solution:
    def checkAlmostEquivalent( word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        for k,v in freq1.items():
            if k in freq2:
                if abs(freq1[k]-freq2[k])>3:
                    return False
            else:
                if freq1[k]>3:
                    return False
                
        for k,v in freq2.items():
            if k in freq1:
                if abs(freq1[k]-freq2[k])>3:
                    return False
            else:
                if freq2[k]>3:
                    return False
        return True
    print(checkAlmostEquivalent(word1 = "", word2 = ""))
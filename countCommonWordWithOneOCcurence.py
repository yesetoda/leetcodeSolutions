class Solution:
    def countWords( words1: list[str], words2: list[str]) -> int:
        distinct1 = []
        for i in words1:
            if words1.count(i) == 1:
                distinct1.append(i)
        for i in words2:
            if words2.count(i) == 1:
                distinct1.append(i)
        count = 0
        for i in distinct1:
            if distinct1.count(i) == 2:
                count+=1
        return count//2
    print(countWords(  words1 = ["a","ab"], words2 = ["a","a","a","ab"] ))
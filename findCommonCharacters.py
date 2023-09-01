from collections import Counter
class Solution:
    def commonChars(words: list[str]) -> list[str]:
        s = words[0]
        for i in range(1,len(words)):
            counter1 = Counter(s)
            counter2 = Counter(words[i])
            s = ''.join(sorted((counter1 & counter2).elements()))
        return list(s)
    print(commonChars( words = ["cool","lock","cook"] ))
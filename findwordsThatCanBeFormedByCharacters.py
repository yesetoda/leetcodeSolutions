class Solution:
    def countCharacters( words: list[str], chars: str) -> int:
        wordcount = 0
        for i in words:
            s = [i for i in chars]
            Found =True
            for j in i:
                if j in s:
                    s.remove(j)
                elif j not in s:
                    Found = False
                    break
                
            if Found:
                wordcount+=len(i)
        return wordcount
    print(countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
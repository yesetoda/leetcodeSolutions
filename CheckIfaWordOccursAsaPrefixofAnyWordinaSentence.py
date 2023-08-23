class Solution:
    def isPrefixOfWord(sentence: str, searchWord: str) -> int:
        ind = 1
        for i in sentence.split():
            print(i,i.startswith(searchWord))
            if i.startswith(searchWord):
                return ind
            ind+=1
        return -1
    print(isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))
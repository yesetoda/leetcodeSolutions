class Solution:
    def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
        mat = {'a':"0", 'b': "1" ,'c': "2", 'd': "3", 'e': "4", 'f': "5", 'g': "6", 'h': "7", 'i': "8", 'j': "9"}
        ind = 0
        fw = ""
        sw = ""
        for i in firstWord+secondWord:
            if ind<len(firstWord):
                fw+=mat[i]
            else:
                sw+=mat[i]
            ind+=1
        tr = ""
        for i in targetWord:
            tr+=mat[i]
        if int(fw)+int(sw) == int(tr):
            return True
        return False
    print(isSumEqual( firstWord = "acb", secondWord = "cba", targetWord = "cdb"))
                
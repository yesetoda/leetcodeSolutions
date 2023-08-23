class Solution:
    def toGoatLatin(sentence: str) -> str:
        out = ''
        ind = 1
        for i in sentence.split():
            if i.lower().startswith('a') or i.lower().startswith('e') or  i.lower().startswith('i') or i.lower().startswith('o') or i.lower().startswith('u'):
                out+=i+"ma"+"a"*ind+" "
            else:
                out+=i[1:]+i[0]+"ma"+"a"*ind+" "
            ind+=1
        return out[:-1]
    print(toGoatLatin(sentence = "I speak Goat Latin"))
class Solution:
    def isLongPressedName(name: str, typed: str) -> bool:
        wordcount = 0
        s = [i for i in typed]
        for i in name:
            Found =True
            if i in s:
                s.remove(i)
            elif i not in s:
                Found = False
                break
        return Found
    print(isLongPressedName(name = "saeed", typed = "ssaaedd"))
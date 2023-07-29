class Solution:
    def decodeMessage( key: str, message: str) -> str:
        sub =""
        for i in key.replace(" ",""):
            if i not in sub:
                sub+=i
        ind = ord("a")
        out =""
        replacementTable = {" ":" "}
        for i in sub:
            replacementTable[i] = chr(ind)
            ind+=1
        for j in message:
            out+=replacementTable[j]
        return out
    key = "eljuxhpwnyrdgtqkviszcfmabo"
    message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    print(decodeMessage(key,message))
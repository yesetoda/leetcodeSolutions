from random import randint
class Solution:
    def minFlips( target: str) -> int:
        s = "0"*len(target)
        cnt = 0
        for i in range(len(target)-1,-1,-1):
            if s[i]!=target[i]:
                chng = target[i]
                cnt +=1
                s = chng*(len(target)-(len(target)-i))+s[i+1:]
        return cnt
    s = ""
    for i in range(10**5):
        s+=str(randint(0,1))
    print(s)
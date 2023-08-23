class Solution:
    def isMatch( s: str, p: str) -> bool:
        ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        chk = [i for i in p]
        s = [i for i in s]
        while chk:
            print(s,chk)
            if (chk[0] !='.' and chk[0]!='*') and len(s)!=len(p):
                return False
            if chk[0] in s[0]:
                s.pop(0)
                chk.pop(0)
            if chk[0] == ".":
                s.pop(0)
                chk.pop(0)
            
                
            
        return True
    print(isMatch(s = "aaaaaaaaaaaaa", p = "aaaaaaaaaaaa."))
            
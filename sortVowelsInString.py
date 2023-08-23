class Solution:
    def sortVowels( s: str) -> str:
        out = ""
        a = sorted([i for i in s if i.lower() in ["a","e","i","o","u"]],reverse = True)
        chk = set(a)
        ind = -1
        for i in s:
            if i in chk:
                out+=a[ind]
                ind-=1
            else:
                out+=i
        return out
    print(sortVowels( s = "lYmpH"))
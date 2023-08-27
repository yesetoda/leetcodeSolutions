class Solution:
    def maximum69Number (num: int) -> int:
        s = str(num)
        if "6" in s:
            ind= s.index("6")
        else:
            return num
        out = s[:ind]+"9"+s[ind+1:]
        return int(out)
    print(maximum69Number(num =  9999))
class Solution:
    def gcdOfStrings( str1: str, str2: str) -> str:
        out = "0"
        for i in range(len(str2),0,-1):
            # print(f"str2[:i] ==>{str2[:i]},str1.count(str2[:i]) ==>{str1.count(str2[:i]) },len(str1),len(str2[:i]) ==>{len(str1),len(str2[:i])},len(str1)/len(str2[:i])==>{len(str1)/len(str2[:i])}")
            x = ""
            for j in out[::-1]:
                if j.isdecimal():
                    x+=j 
                else:
                    break
            y = str1.count(str2[:i])
            if str1.count(str2[:i]) == int(len(str1)/len(str2[:i])):
                if int(x)< len(str2[:i]):
                    out = str2[:i]+str(y)
                    # print(out)
            ind  = 0
            for j in range(len(out[::-1])):
                if out[j].isalpha():
                    ind = j
        return out[:j]
    print(gcdOfStrings(str1 = "LEET", str2 = "CODE"))
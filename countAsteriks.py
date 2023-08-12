class Solution:
    def countAsterisks( s: str) -> int:
        for i in range(int(s.count("|")/2)):
            ind1 = s.index("|")
            ind2 = s[ind1+1:].index("|")
            pre = s[:ind1]
            post = s[ind2+ind1+2:]
            # print(f"ind1 ==>{ind1} ind2==>{ind2} pre ==>{pre}  post ==> {post}")
            s = pre+post
            # print(s)
            if "|" not in s:
                break
        return s.count("*")
    print(countAsterisks(s = "yo|uar|e**|b|e***au|tifu|l|yeneineh*|*"))
class Solution:
    def maxDistance(colors: list[int]) -> int:
        chk = set(colors)
        rev = {i:len(colors)-1-colors[::-1].index(i) for i in chk}
        mx=  0
        for i in chk:
            for j in chk:
                if i==j:
                    continue
                val = rev[i] - colors.index(j)
                if val>mx:
                    mx = val
        return mx
    print(maxDistance(colors = [0,1]))
class Solution:
    def largestInteger( num: int) -> int:
        n = str(num)
        out = []
        odds= []
        evens = []
        inds = []
        for i in n:
            if int(i)%2 == 0:
                inds.append(True)
                evens.append(i)
            else:
                inds.append(False)
                odds.append(i)
        odds.sort()
        evens.sort()
        for i in inds:
            if i:
                out.append(evens.pop())
            else:
                out.append(odds.pop())
        return int("".join(out))
    print(largestInteger(num = 13247234980234689))
    print(sorted([6,2,6,5,1,2]))
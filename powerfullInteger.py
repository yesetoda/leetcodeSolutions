
class Solution:
    def powerfulIntegers(x: int, y: int, bound: int) -> list[int]:
        # out = set()
        # i,j = 0,0
        # while True:
        #     if x ** i + y ** j <= bound:
        #         out.add(x ** i + y ** j)
        #         j += 1
        #     elif i + 1 <= bound and x ** (i + 1) + y ** 0 <= bound:
        #         i += 1
        #         j = 0
        #     else:
        #         return list(out)
        out = set()
        i, j = 0, 0
        while x ** i <= bound:
            while x ** i + y ** j <= bound:
                out.add(x ** i + y ** j)
                j += 1
                if y == 1:
                    break
            i += 1
            j = 0
            if x == 1:
                break

        return list(out)
    print(powerfulIntegers(x = 1, y =2, bound = 10**6))
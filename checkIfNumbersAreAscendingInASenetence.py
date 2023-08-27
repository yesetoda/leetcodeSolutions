class Solution:
    def areNumbersAscending( s: str) -> bool:
        prev = -1
        cur = -1
        for i in s.split():
            if i.isdigit():
                cur = int(i)
                if prev< cur:
                    prev = cur
                else:
                    return False
        return True
    print(areNumbersAscending( s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles 9"))
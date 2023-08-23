def checkDistances(s: str, distance: list[int]) -> bool:
    for i in set(s):
        if s.rindex(i) - s.index(i) - 1 != distance[ord(i) - 97]:
            return False
    return True

print(checkDistances(s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
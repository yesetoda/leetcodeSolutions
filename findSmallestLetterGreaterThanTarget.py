from time import perf_counter
class Solution:
    def nextGreatestLetter( letters: list[str], target: str) -> str:
        greats = []
        for i in set(letters):
            if ord(i)>ord(target):
                greats.append(i)
                # print(greats)
        return min(greats) if greats else letters[0]
    a = perf_counter()
    print(nextGreatestLetter(letters = ["x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y","x","x","y","y"], target = "z"))
    b = perf_counter()
    print(b-a)
    print(0.0004656999999497202,0.0013000999997530016)
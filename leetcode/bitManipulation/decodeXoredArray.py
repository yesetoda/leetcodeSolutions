class Solution:
    def decode(encoded: list[int], first: int) -> list[int]:
        out = [first]
        prev = first
        for i in encoded:
            prev = prev^i
            out.append(prev)
        return out
    print(decode(encoded = [6,2,7,3], first = 3))

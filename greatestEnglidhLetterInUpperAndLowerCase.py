class Solution:
    def greatestLetter( s: str) -> str:
        out = chr(63)
        x = set([i for i in s])
        for i in x:
            if i.lower() in x and i.upper() in x:
                if ord(out)<ord(i):
                    out = i
        return out.upper() if ord(out)>63 else ""
    print(greatestLetter( s = "AbCdEfGhIjK"))
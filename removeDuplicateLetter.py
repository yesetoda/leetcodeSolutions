class Solution:
    def removeDuplicateLetters(s: str) -> str:
        # return "".join(sorted(set(s)))
        out = ""
        final = len(set(s))
        for i in s[::-1]:
            if len(out)<final:
                if i not in out:
                    out+=i
            print(out)
        return out[::-1]
    print(removeDuplicateLetters(s = "cbacdcbc"))
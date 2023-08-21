class Solution:
    def halvesAreAlike( s: str) -> bool:
        leng = len(s)
        left = 0
        right = 0
        for i in  ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            left +=s[:leng//2].count(i)
            right+= s[leng//2:].count(i)
        return left==right
    print(halvesAreAlike(s = "book"))
class Solution:
    def repeatedCharacter(s: str) -> str:
        freq = {}
        for i in s:
            if i not in freq.keys():
                freq[i] = 1
            else:
                return i
    print(repeatedCharacter(s = "abcdd"))
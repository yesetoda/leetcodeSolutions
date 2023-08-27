class Solution:
    def minTimeToType(word: str) -> int:
        ptr = 'a'
        secs = 0
        for char in word:
            diff = abs(ord(ptr) - ord(char))
            secs += min(diff, 26 - diff) + 1
            ptr = char
        return secs
    print(minTimeToType( word = "bza" ))
            
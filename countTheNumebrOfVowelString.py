class Solution:
    def vowelStrings( words: list[str], left: int, right: int) -> int:
        v = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        for i in range(left,right+1):
            if words[i][0] in v and words[i][-1] in v:
                count+=1
                
        return count
    print(vowelStrings(words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4))
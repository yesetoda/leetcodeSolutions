class Solution:
    def sortString(s: str) -> str:
        srt = sorted(list(set(s)))
        for i in sorted(s):
            srt.append(i)
    print(sortString(s = "aaaabbbbcccc"))
            

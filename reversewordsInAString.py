class Solution:
    def reverseWords( s: str) -> str:
        return " ".join(s.strip().split()[::-1])
    print(reverseWords(s  = "a good   example"))
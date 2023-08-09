class Solution:
    def reverseWords(s: str) -> str:
        slist = s.split()
        rslist = [i[::-1] for i in slist]
        return ' '.join(rslist)
    print(reverseWords( s = "Let's take LeetCode contest"))
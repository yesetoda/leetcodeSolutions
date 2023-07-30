class Solution:
    def mostWordsFound( sentences: list[str]) -> int:
        return max([len(i.split())for i in sentences])
    print(mostWordsFound(sentences = ["please wait", "continue to fight", "continue to win"]))
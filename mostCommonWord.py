from collections import Counter
class Solution:
    def mostCommonWord( paragraph: str, banned: list[str]) -> str:
        para = ""
        for i in paragraph.lower():
            if i in "!?',;. ":
                para+=" "
            else:
                para+=i
        para = list(set(para.split()))
        for i in para[:]:
            if i in banned:
                para.pop(para.index(i))
        return Counter(para).most_common(1)[0][0]
    print(mostCommonWord(  "Bob hit a ball, the hit BALL flew far after it was hit.",banned =["hit"]))
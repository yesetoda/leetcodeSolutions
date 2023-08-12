# from collections import Counter 
# class Solution:
#     def frequencySort( s: str) -> str:
#         freq = Counter(s)
#         print(freq)
#         out = ""
#         for i,j in freq.items():
#             print(i,j)
#             out += (i)*j
#             print(out)
#         return out
    # print(frequencySort(s = "tree"))
from collections import Counter

class Solution:
    def frequencySort( s: str) -> str:
        freq = Counter(s)
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        out = ""
        for char, count in sorted_items:
            out += char * count
        return out
    print(frequencySort(s = "tree"))
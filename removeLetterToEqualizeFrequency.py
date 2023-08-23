# from collections import Counter
# class Solution:
#     def equalFrequency(word: str) -> bool:
#         freq = Counter(word)

#         if len(freq) == 1:
#             return True
        
#         if len(freq) > 2:
#             return False
        
#         values = list(freq.values())
#         keys = list(freq.keys())
#         if values[0] == 1 or values[1] == 1:
#             return True
        
#         return False
#     print(equalFrequency(word = "ddaccb"))

from collections import Counter

def canEqualizeFrequency(word: str) -> bool:
    freq = Counter(word)
    frequencies = list(freq.values())
    if len(set(frequencies)) == 1:
        return True
    if len(set(frequencies)) > 2:
        return False
    f1, f2 = set(frequencies)
    if (frequencies.count(f1) == 1 and f1 == 1) or (frequencies.count(f2) == 1 and f2 == 1):
        return True
    if abs(f1 - f2) == 1:
        return True
    return False
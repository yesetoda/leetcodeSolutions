from collections import Counter
class Solution:
    def uniqueOccurrences( arr: list[int]) -> bool:
        tr1 = Counter(arr).values()
        return len(list(tr1)) == len(set(tr1))
    print(uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))
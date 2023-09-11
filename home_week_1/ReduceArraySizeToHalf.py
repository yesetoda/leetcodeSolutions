from collections import Counter
class Solution:
    def minSetSize(arr: list[int]) -> int:
        el_freq = {}
        for i in set(arr):
            el_freq[i] = arr.count(i)
        el_freq = sorted(el_freq,key =lambda x:el_freq[x])
        print(el_freq)
    print(minSetSize( arr = [3,3,3,3,5,5,5,2,2,7]))
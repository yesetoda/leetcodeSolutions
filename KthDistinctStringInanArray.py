class Solution:
    def kthDistinct(arr: list[str], k: int) -> str:
        distinct = []
        for i in arr:
            if arr.count(i) == 1:
                distinct.append(i)
        # print(distinct)
        return distinct[k-1] if k<=len(distinct) else ""
    print(kthDistinct( arr = ["d","b","c","b","c","a"], k = 2 ))
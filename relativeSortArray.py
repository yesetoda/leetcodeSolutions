class Solution:
    def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
        out = []
        for i in arr2:
            for j in range(arr1.count(i)):
                out.append(i)
        sortable = []
        for i in set(arr1).difference(set(arr2)):
            for j in range(arr1.count(i)):
                sortable.append(i)
        out.extend(sorted(sortable))
        return out
    print(relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))
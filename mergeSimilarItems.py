class Solution:
    def mergeSimilarItems( items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        dicto = {}
        out = []
        for i in items1:
            dicto[i[0]] = i[1]
        for i in items2:
            if i[0] in list(dicto.keys()):
                dicto[i[0]] += i[1]
            else:
                dicto[i[0]] = i[1]
        lst = list(dicto.keys())
        lst.sort()
        for i in lst:
            out.append([i,dicto[i]])
        return out
    array1= [[i, 1] for i in range(1, 1001)]
    print(mergeSimilarItems(array1, items2 = [[2,1],[3,2],[1,3]]))


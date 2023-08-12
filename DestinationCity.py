class Solution:
    def destCity(paths: list[list[str]]) -> str:
        cities = set(i[0] for i in  paths)
        print(cities)
        for i in paths:
            if i[1] not in cities:
                return i[1]
    print(destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
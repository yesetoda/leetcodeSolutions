class Solution:
    def maximumPopulation(logs: list[list[int]]) -> int:
        year = {}
        for i in logs:
            for j in logs:
                if i[0]<=j[0] and i[1]>j[0]:
                    
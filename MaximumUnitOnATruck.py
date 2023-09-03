class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        mx = [[i[0]*i[1],i[0]] for i in boxTypes]
        mx.sort()
        for i in mx:
            
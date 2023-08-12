class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start = newInterval[0]
        end = newInterval[1]
        ind = 0
        while (start > intervals[ind][0]) and  (start > intervals[ind][1] ):
            ind+=1
        while (end > intervals[ind][0]) and  (start > intervals[ind][1] ):
            
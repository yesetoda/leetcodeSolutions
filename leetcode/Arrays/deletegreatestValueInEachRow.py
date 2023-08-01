class Solution:
    def deleteGreatestValue( grid: list[list[int]]) -> int:
        mx = []
        
        for i in grid:
            mx.append(max(i))
            del grid[grid.index(mx)]
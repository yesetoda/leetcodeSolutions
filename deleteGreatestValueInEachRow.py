class Solution:
    def deleteGreatestValue(grid: list[list[int]]) -> int:
        result = 0
        while grid[0]:
            mx = []
            for i in range(len(grid)):
                # print(grid[i])
                mx.append(max(grid[i]))
                # print(mx)
                grid[i].remove(max(grid[i]))
                # print(grid,result)
            result += max(mx)
            
        return result
    print(deleteGreatestValue(grid = [[0],[1]]))
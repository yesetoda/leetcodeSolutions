class Solution:
    def largestLocal( grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                submatrix = [
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                    grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                ]
                maxLocal[i][j] = max(submatrix)
        
        return maxLocal
    print(largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    #         row = grid[i]
    #         for j in range(leng):
    #             row.append(grid[j][i])
    #         print(row)
    #         out.append(max(row))
    #     x = leng-2
    #     printable = [0]*x
    #     ind = 0
    #     for i in range(x):
            
    #         print(ind,x,out,out[ind:ind+x])
    #         printable[i] = out[ind:ind+x]
    #         ind+=x
    #     print(printable)
    #     return printable
    # print()
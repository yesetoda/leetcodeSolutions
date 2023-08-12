class Solution:
    def largestLocal( grid: list[list[int]]) -> list[list[int]]:
        out  = []
        leng = len(grid)
        for i in range(leng):
            row = grid[i]
            for j in range(leng):
                row.append(grid[j][i])
            print(row)
            out.append(max(row))
        x = leng-2
        printable = [0]*x
        ind = 0
        for i in range(x):
            
            print(ind,x,out,out[ind:ind+x])
            printable[i] = out[ind:ind+x]
            ind+=x
        print(printable)
        return printable
    print(largestLocal(grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
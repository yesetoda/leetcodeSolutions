class Solution:
    def oddCells( m: int, n: int, indices: list[list[int]]) -> int:
        mat = [[0 for i in range(n)]for i in range(m)] 
        for i in indices:
            for col in range(n):
                mat[i[0]][col]+=1
            for row in range(m):
                mat[row][i[1]]+=1
        count = 0
        for i in mat:
            for j in i:
                if j%2==1:
                    count+=1
        return count
    print(oddCells(m = 2, n = 2, indices = [[1,1],[0,0]]))
class Solution:
    def diagonalSort( mat: list[list[int]]) -> list[list[int]]:
        row = len(mat)
        col = len(mat[0])
        step = [[i, 0] for i in range(row-1, -1, -1)] + [[0, j] for j in range(1, col)]
        
        for i in step:
            ind = i[:]
            diagonal = []
            
            while ind[0] < row and ind[1] < col:
                diagonal.append(mat[ind[0]][ind[1]])
                ind[0] += 1
                ind[1] += 1
            
            diagonal.sort()
            ind = i[:]
            for num in diagonal:
                mat[ind[0]][ind[1]] = num
                ind[0] += 1
                ind[1] += 1
        return mat
    print(diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
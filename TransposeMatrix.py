class Solution:
    def transpose( matrix: list[list[int]]) -> list[list[int]]:
        newmat = [[-10**9-1 for  i in range(len(matrix))]for  i in range(len(matrix[0]))]
        print(newmat)
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                newmat[col][row] = matrix[row][col]
        return newmat
    print(transpose(matrix = [[1],[4]]))
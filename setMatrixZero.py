# class Solution:
#     def setZeroes( matrix: list[list[int]]) -> None:
#         m = matrix[:]
        
#         for i in range(len(m)):
#             # print(m[i])
#             if 0 in m[i]:
#                 colInd = m[i].index(0)
#                 # print(colInd)
#                 matrix[i] = [0]*len(m[i])
#                 for j in range(len(m[i])):
#                     if matrix[j][colInd] ==0:
#                         pass
#                     else:
#                         matrix[j][colInd] = 0
#             # print(matrix[i])
                    
#         print(matrix)
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#     setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])

import copy

class Solution:
    def setZeroes( matrix: list[list[int]]) -> None:
        m = copy.deepcopy(matrix)
        first_row_zero = False
        first_col_zero = False
        if 0 in matrix[0]:
            first_row_zero = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[i])
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if first_row_zero:
            matrix[0] = [0] * len(matrix[0])
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        print(matrix)
    setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])
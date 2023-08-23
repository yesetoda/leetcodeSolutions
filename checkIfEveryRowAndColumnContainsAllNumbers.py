# class Solution:
#     def checkValid(matrix: list[list[int]]) -> bool:
#         leng = len(matrix)
#         correct = [i for i in range(1,leng+1)]
#         for i in matrix:
#             if sorted(i) != correct:
#                 return False
#         return True


def checkValid(matrix: list[list[int]]) -> bool:
    leng = len(matrix)
    correct = set(range(1, leng + 1))

    for row in matrix:
        if set(row) != correct:
            return False

    for col in range(leng):
        if set(matrix[row][col] for row in range(leng)) != correct:
            return False

    subgrid_size = int(leng ** 0.5)
    for start_row in range(0, leng, subgrid_size):
        for start_col in range(0, leng, subgrid_size):
            subgrid = []
            for row in range(start_row, start_row + subgrid_size):
                subgrid.extend(matrix[row][start_col:start_col + subgrid_size])
            if set(subgrid) != correct:
                return False

    return True
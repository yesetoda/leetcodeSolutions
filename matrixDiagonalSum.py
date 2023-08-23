class Solution:
    def diagonalSum( mat: list[list[int]]) -> int:
        out = 0
        leng = len(mat)
        for i in range(leng):
            out+=mat[i][i]+mat[i][leng-1-i]
        return out-mat[leng//2] if leng%2==1 else out
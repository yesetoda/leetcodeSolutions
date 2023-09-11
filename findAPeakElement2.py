class Solution:
    def findPeakGrid( mat: list[list[int]]) -> list[int]:
        mx = [-1,-1]
        mxval = 0
        if len(mat)<=2:
            for i in range(len(mat)):
                val = max(mat[i])
                if mxval<val:
                    mx[0] =i
                    mx[1] = mat[i].index(val)
            return mx
        mx = 0
        for i in range(1,len(mat)):
            for j in range(len(mat[i])-1):
                val = mat[i][j]
                print(val)
                if mat[i][j-1]<val and mat[i][j+1]<val and mat[i-1][j]<val and mat[i+1][j]<val :
                    return [i,j]
    print(findPeakGrid([[1,4],[3,2]]))
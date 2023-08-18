class Solution:
    def searchMatrix( matrix: list[list[int]], target: int) -> bool:
        x = ""
        for i in matrix:
            x+="".join(map(str,i))
        print(x.split())
        return str(target) in x.split()
    print(searchMatrix(matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5))
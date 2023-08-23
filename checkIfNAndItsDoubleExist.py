class Solution:
    def checkIfExist( arr: list[int]) -> bool:
        s = set(arr)
        for i in range(len(arr)):
            if  arr[i]*2 in s:
                if arr.index(arr[i]*2) != i:
                    return True
        return False
    print(checkIfExist([0,1,3,5,7,0]))
class Solution:
    def findTheDistanceValue( arr1: list[int], arr2: list[int], d: int) -> int:
        mx = 0
        for i in arr1:
            for j in arr2:
                print(i,j,i-j,mx,i-j <= d)
                if abs(i-j) <= d:
                    if i-j>mx:
                        mx= i-j
        return mx
    print(findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6))

from statistics import mean
class Solution:
    def trimMean( arr: list[int]) -> float:
        arr = sorted(arr)
        fivePercent = int(len(arr)*0.05)
        arr = arr[fivePercent:-fivePercent]
        return mean(arr)
    
        # n=int(0.05*len(arr))
        # for i in range(n):
        #     arr.remove(min(arr))
        #     arr.remove(max(arr))
        # return sum(arr)/len(arr)
    print(trimMean(arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))
        
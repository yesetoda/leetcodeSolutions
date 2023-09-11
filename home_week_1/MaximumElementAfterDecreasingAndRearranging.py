from random import randint

class Solution:
    def maximumElementAfterDecrementingAndRearranging(arr: list[int]) -> int:
        count = 0
        arr[0] = 1
        
        srt = sorted(arr[:])
        for i in range(len(arr)-1):
            if arr[i]!=srt[i]:
                mnind = i+arr[i:].index(min(arr[i+1:]))
                arr[i],arr[mnind] = min(arr[i+1:]),arr[i]
                count+=1 
        print(arr,count)
        for j in range(1,len(arr)):
            if arr[j]-arr[j-1]>1:
                count+=1
                arr[j] = arr[j-1]
        print(arr,count)
        return count 
    def maximumElementAfterDecrementingAndRearranging2(arr: list[int]) -> int:
        arr.sort()
        
        # make sure the first value is 1
        arr[0] = 1

        # after each consecutive value make sure difference is not more than one
        for i in range(1, len(arr) ):

            # difference > 1, so decrease the value and make the difference 1
            # making the difference one helps to get maximum possible value
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1]+1
        print(arr)
        return arr[-1]
    arr =[2,3,4,5,3,5,32]

    print(maximumElementAfterDecrementingAndRearranging(arr))
    print(maximumElementAfterDecrementingAndRearranging2(arr))
    
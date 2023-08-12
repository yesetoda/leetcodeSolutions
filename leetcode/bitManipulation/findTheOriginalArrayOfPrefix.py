class Solution:
    def findArray(pref):
        n = len(pref)
        arr = [0] * n
        arr[0] = pref[0]

        for i in range(1, n):
            arr[i] = pref[i] ^ arr[i-1]

        return arr
    print(findArray(pref = [5,2,0,3,1]))
    

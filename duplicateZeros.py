class Solution:
    def duplicateZeros(arr: list[int]) -> None:
        length = len(arr)
        zero_count = arr.count(0)
        ind = 0
        if zero_count > 0:
            while ind < length:
                if arr[ind] == 0:
                    arr.insert(ind + 1, 0)
                    ind += 2
                else:
                    ind += 1

            # Trim the array to the original length
            arr[:] = arr[:length]
            return arr
    print(duplicateZeros( arr = [1,0,2,3,0,1,0,4,5,0]))
            
        
    
    
    """
    Do not return anything, modify arr in-place instead.
    """
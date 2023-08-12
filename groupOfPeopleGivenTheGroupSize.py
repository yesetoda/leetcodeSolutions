class Solution:
    def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
        groups = {}
        result = []
        
        for i, size in enumerate(groupSizes):
            if size in groups:
                groups[size].append(i)
            else:
                groups[size] = [i]
            
            if len(groups[size]) == size:
                result.append(groups.pop(size))
        
        return result
                
                
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(groupThePeople(groupSizes))
    # Output: [[5], [0, 1, 2], [3, 4, 6]]

    groupSizes = [2, 1, 3, 3, 3, 2]
    print(groupThePeople(groupSizes))
    # Output: [[1], [0, 5], [2, 3, 4]]
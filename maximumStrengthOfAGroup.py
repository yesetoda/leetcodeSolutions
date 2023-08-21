# from typing import List

# class Solution:
#     def maxStrength(nums: List[int]) -> int:
#         ng = []
#         out = 1
#         if len(nums) == 1:
#             return nums[0]
#         for i in sorted(nums):
#             if i > 0:
#                 out *= i
#             elif i < 0:
#                 ng.append(i)
#         if ng:
#             ng.sort()
#             if len(ng) % 2 == 0:
#                 for i in ng:
#                     out *= i
#             else:
#                 if len(ng) == 1:
#                     return out
#                 else:
#                     for i in ng[:-1]:
#                         out *= i
#         return out
#     print(maxStrength(nums = [-1,0,-4]))

from itertools import permutations

def find_max_multiple(numbers):
    # Generate all possible permutations of the numbers
    permutations_list = permutations(numbers)
    
    max_multiple = float('-inf')  # Initialize with negative infinity
    
    # Iterate through each permutation
    for permutation in permutations_list:
        # Generate the multiple by multiplying the elements in the permutation
        multiple = 1
        for num in permutation:
            multiple *= num
        
        # Update max_multiple if the current multiple is greater
        if multiple > max_multiple:
            max_multiple = multiple
    
    return max_multiple

# Example usage
numbers = [0, -3, 4]
print(result := find_max_multiple(numbers))
# print(f"The maximum multiple that can be generated from {numbers} is: {result}")
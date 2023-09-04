# class Solution:
#     def numberOfMatches( n: int) -> int:
#         matches = 0
#         while n>1:
#             # print(n,matches)
#             if n%2==0:
#                 n//=2
#                 matches+=n
#             else:
#                 n = (n-1)//2
#                 matches += n
#                 n+=1
#         return matches
#     print(numberOfMatches(14))

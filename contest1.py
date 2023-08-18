# class Solution:
#     def firstUniqChar(s: str) -> int:
#         for i in s:
#             # print(i,s.count(i))
#             if s.count(i)==1:
#                 return s.index(i)
#         return -1
#     print(firstUniqChar(s = "loveleetcode"))


class Solution:
    def lexicalOrder(n: int) -> list[int]:
        l = [str(i) for i in range(1,n+1)]
        l = [int(i) for i in sorted(l)]
        return l
    print(lexicalOrder(13))
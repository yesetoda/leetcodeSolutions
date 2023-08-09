# class Solution:
#     def makeGood(s: str) -> str:
#         out = []
#         i = 0
#         while i < len(s):
#             if i < len(s) - 1:
#                 j = i + 1
#             if i ==len(s)-1:
#                 j = i
#             if s[i].upper() == s[j] :
#                 if i + 2 < len(s) - 1:
#                     i += 2
#                 else:
#                     break
#             else:
#                 out.append(s[i])
#                 i += 1

#         return ''.join(out)


# print(Solution.makeGood(s="abBAcC"))

class Solution:
    def makeGood(s: str) -> str:
        out = []
        for char in s:
            if out and out[-1].lower() == char.lower() and out[-1] != char:
                out.pop()
            else:
                out.append(char)
        return ''.join(out)

print(Solution.makeGood(s="abBAcC"))
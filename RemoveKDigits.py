class Solution:
    def removeKdigits(num: str, k: int) -> str:
        leng = len(num)
        zer = leng
        if k == leng:
            return "0"
        if "0" in num:
            zer = num.index("0")-1
        x = [i for i in num]
        for i in range(k):
            if len(x)>0 and x.index(max(x[:leng-k]))<zer:
                x.pop(x.index(max(x[:leng-k+1])))
            else:
                x.pop(zer)
            while len(x)>1 and x[0] == "0":
                x.pop(0)
        return "".join(x)
# class Solution:
#     def removeKdigits(num: str, k: int) -> str:
#         leng = len(num)
#         zer = leng
#         if k == leng:
#             return "0"
#         if "0" in num:
#             zer = num.index("0") - 1
#         x = [i for i in num]
#         for i in range(k):
#             if len(x) > 0 and x.index(max(x[:leng - k + 1])) <= zer:
#                 x.pop(x.index(max(x[:leng - k + 1])))
#                 zer -= 1
#             else:
#                 x.pop(zer - 1)
#         while len(x) > 1 and x[0] == "0":
#             x.pop(0)
#         return "".join(x)

    print(removeKdigits("1432219", 3))
    print(removeKdigits("112", 1))
    print(removeKdigits("100", 1))
    print(removeKdigits("93483249",1))
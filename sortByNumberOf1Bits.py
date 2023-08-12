# class Solution:
#     def sortByBits(arr: list[int]) -> list[int]:
#         feq = {str(i):str(bin(i)[2:]).count("1") for i in arr}
#         sfeq = list(feq.values())
#         sfeq.sort(reverse = True)
#         out = []
#         for i in sfqe:
#             out.append()
#         # b = [str(bin(i)[2:]).count("1") for i in arr]
#         ind = 0
#         print(feq,sfeq)
#         # for i in arr:
#         #     freq
#     sortByBits([0,1,2,3,4,5,6,7,8])

class Solution:
    def sortByBits(arr: list[int]) -> list[int]:
        # feq = {str(i): str(bin(i)[2:]).count("1") for i in arr}
        sfeq = sorted(arr, key=lambda x: (str(bin(x)[2:]).count("1"), x))
        return sfeq

print(Solution.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1]))
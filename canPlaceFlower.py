# class Solution:
#     def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
#         for i in range(len(flowerbed)):
#             if n>(len(flowerbed)+1)/2:
#                 return False
#             # elif flowerbed[i] ==1:
#             #     pass
#             elif flowerbed[0] == 0 and flowerbed[1]==0:
#                     n-=1
#                     flowerbed[i] = 1
#                     print("c1")

#             elif i>0 and i<len(flowerbed)-1:
#                     if flowerbed[i-1] == 0 and flowerbed[i+1] ==0:
#                         n -=1
#                         flowerbed[i] = 1
#                         print("c3")
#             elif   i == len(flowerbed)-1:
#                 if flowerbed[-1] == 0 and flowerbed[-2]==0:
#                     n-=1
#                     flowerbed[i] = 1
#                     print("c2")

#         print(flowerbed)
#         # print(out)
#         if n <= 0:
#             return True
#         return False
#     print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
                
            
class Solution:
    def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if n <= 0:
                return True

            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1

        return n <= 0

print(Solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1))
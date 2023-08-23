# class Solution:
#     def countPoints(rings: str) -> int:
#         rods  = {f"{i}":"" for i in range(10)}
#         for i in range(0,len(rings),2):
#             if rings[i] not in rods[ rings[i+1]]:
#                 rods[rings[i+1]]+=rings[i]
#         count = 0
#         # print(rods)
#         for i in rods.keys():
#             if "B" in rods[i] and  "R" in rods[i] and  "G" in rods[i] :
#                 count+=1
#         return count
#     print(countPoints("B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9"))

class Solution:
    def countPoints( rings: str) -> int:
        rods  = {f"{i}":"" for i in range(10)}
        for i in range(0,len(rings),2):
            if rings[i] not in rods[ rings[i+1]]:
                rods[rings[i+1]]+=rings[i]
        count = 0
        for i in rods.items():
            if "B" in rods[i] and  "R" in rods[i] and  "G" in rods[i] :
                count+=1
        return count
    print(countPoints("B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9B0B6G0R6R0R6G9"))

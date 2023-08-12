# class Solution:
#     def garbageCollection(garbage: list[str], travel: list[int]) -> int:
#         out = 0
#         types_of_g = ["G","M","P"]
#         for j in range(len(types_of_g)):
#             if j>0:
#                 print(f"output of truck {out}",types_of_g[j])
#             for i in range(len(garbage)):
#                 print(f"from {i} to {i+1}",types_of_g[j] ,"".join(garbage[i:]),types_of_g[j] not in "".join(garbage[i:]))
#                 if types_of_g[j] not in "".join(garbage[i:]):
#                     print(f"no more {types_of_g[j]} garbage")
#                     break
#                 if i>0:
#                         out+=travel[i-1]
#                 if  types_of_g[j] in garbage[i]:
#                     out+=1
#                 elif  types_of_g[j] in garbage[i]:
#                     out+=1
#                 elif  types_of_g[j] in garbage[i]:
#                     out+=1
#                 print(out)
#         print(f"output of truck {out}")
#         return out+1
#     print(garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))


class Solution:
    def garbageCollection(garbage: list[str], travel: list[int]) -> int:
        out = 0
        types_of_g = ["G", "M", "P"]
        truck_times = [0, 0, 0]  # Track total times for each truck
        
        for j in range(len(types_of_g)):
            collected_garbage = set()
            for i in range(len(garbage)):
                if types_of_g[j] in garbage[i]:
                    collected_garbage.add(types_of_g[j])
                    out += 1
                    if i > 0:
                        truck_times[j] += travel[i - 1]
                if collected_garbage == {"G", "M", "P"}:
                    break
        
        max_time = max(truck_times)  # Find the maximum time among all trucks
        return out + max_time
    print(garbageCollection(garbage=["MMM", "PGM", "GP"], travel=[3, 10]))
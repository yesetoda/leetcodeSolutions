# # from math import sqrt

# # class Solution:
# #     def findPrimePairs( n: int) -> list[list[int]]:
# #         # x = PrimesUpTo2(n)
# #         # print(x)
# #         primes = [True]*(n+1)
# #         primes[0],primes[1] =False,False
# #         for i in range(2,int(sqrt(n))+1):
# #             if primes[i] == False:
# #                 continue
# #             for j in range(i,int(n/i)+1):
# #                 primes[i*j] = False
# #         x = [ind for ind,bl in enumerate(primes) if bl]
# #         out = []
# #         for i in x:
# #             for j in x:
# #                 if i+j == n:
# #                     if [i,j] not in out and [j,i] not in out :
# #                         out.append([i,j])
# #         return out
# #     print(findPrimePairs(10**6))
  
# from math import isqrt
# from time import perf_counter

# class Solution:
#     def findPrimePairs(n: int) -> list[list[int]]:
#         def is_prime(num):
#             if num < 2:
#                 return False
#             if num == 2:
#                 return True
#             if num % 2 == 0:
#                 return False
#             for i in range(3, isqrt(num) + 1, 2):
#                 if num % i == 0:
#                     return False
#             return True
#         s1 = perf_counter()
#         # out = []
#         # primes = [num for num in range(n + 1) if is_prime(num)]
#         # for i in primes:
#         #     if is_prime(n-i):
#         #         if [i,n-i] not in out and [n-i,i] not in out:
#         #             out.append([i,n-i])
        
#         # primes = set(num for num in range(2, n) if is_prime(num))
#         # print(primes)
#         # out = []
#         # for i in range(2, (n // 2) + 1):
#         #     if i in primes and (n - i) in primes:
#         #         out.append([i, n - i])
#         #         print(out)
        
#         out = []
#         for i in range(2, (n // 2) + 1):
#             if is_prime(i) and is_prime(n - i):
#                 out.append([i, n - i])
#         print(out)
#         s2 = perf_counter()
#         print(s2-s1)
        
        
#         return out

#     print(findPrimePairs(1009887))



from math import isqrt
from typing import List

class Solution:
    def findPrimePairs(n: int) -> List[List[int]]:
        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, isqrt(num) + 1, 2):
                if num % i == 0:
                    return False
            return True

        primes = set(num for num in range(2, n) if is_prime(num))

        out = []
        added_pairs = set()
        for i in range(2, (n // 2) + 1):
            if i in primes and (n - i) in primes:
                pair = [i, n - i]
                pair.sort()
                pair_tuple = tuple(pair)
                if pair_tuple not in added_pairs:
                    out.append(pair)
                    added_pairs.add(pair_tuple)
        return out
    print(findPrimePairs(9999996))
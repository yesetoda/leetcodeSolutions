from math import log2
class Solution:
    def minOperations( n: int) -> int:
        # opcount = 0
        # if n % 2 == 1:
        #     n -= 1
        #     opcount += 1
        # while n != 0:
        #     if n > 0:
        #         if abs(n - 2 ** (int(log2(n)))) > abs(n - 2 ** ((int(log2(n)) + 1))):
        #             n -= 2 ** (int(log2(n)) + 1)
        #         else:
        #             n -= 2 ** (int(log2(n)))
        #         opcount += 1
        #     elif n < 0:
        #         if abs(-n - 2 ** (int(log2(-n)))) > abs(-n - 2 ** ((int(log2(-n)) + 1))):
        #             n += 2 ** (int(log2(-n)) + 1)
        #         else:
        #             n += 2 ** (int(log2(-n)))
        #         opcount += 1
        # return opcount
        # return bin(n).count('1')
        operations = 0
        while n > 0:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1
            operations += 1
        return operations
    print(minOperations(n =2))

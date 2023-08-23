from math import sqrt


class Solution:
    # def countPrimes( n: int) -> int:
    #     primes = [True]*(n+1)
    #     primes[0],primes[1] =False,False
    #     # print(primes)
    #     for i in range(2,int(sqrt(n))+1):
    #         # print("out",i,primes)
    #         if primes[i] == False:
    #             continue
    #         for j in range(2*i,int(n/i)+1):
    #             primes[i*j] = False
    #             # print(i,j,i*j,primes)
    #     out = [ind for ind,bl in enumerate(primes) if bl]
    #     return out
    def PrimesUpTo(n):
        n = n-1
        if n<2:
            return 0
        primes = [True]*(n+1)
        primes[0],primes[1] =False,False
        for i in range(2,int(sqrt(n))+1):
            if primes[i] == False:
                continue
            for j in range(i,int(n/i)+1):
                primes[i*j] = False
        x = primes.count(True)
        return x
    print(PrimesUpTo(10**6))
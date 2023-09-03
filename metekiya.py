from time import perf_counter
import sys


initial = perf_counter()
def fabo(n,memo = {},mete = [0]):
    mete[0]+=1
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    else:
        memo[n] = fabo(n-1,memo,mete)+fabo(n-2,memo,mete)
    return mete[0]
print(fabo(41))
final = perf_counter()
print(final-initial)


def fabo2(n,mete = [0]):
    mete[0]+=1
    if n<=2:
        return 1
    else:
        x = fabo2(n-1,mete)+fabo2(n-2,mete)
    return mete[0]
i= perf_counter()
print(fabo2(41))
f= perf_counter()
print(f-i)



class Solution:
    def fib( n):
        out = 0
        if n<=1:
            out+= n
        fprev = 0
        fcurr = 1
        for i in range(2,n+1):
            out=fprev+fcurr
            fprev = fcurr
            fcurr = out
        return out
    print(fib(10))
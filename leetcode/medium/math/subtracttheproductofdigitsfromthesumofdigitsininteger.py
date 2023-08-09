class Solution:
    def subtractProductAndSum( n: int) -> int:
        sumd =0
        muld = 1
        for i in str(n):
            sumd +=int(i)
            muld *=int(i)
        return muld-sumd
    print(subtractProductAndSum(n = 4421))
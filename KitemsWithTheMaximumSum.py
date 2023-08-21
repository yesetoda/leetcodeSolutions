class Solution:
    def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        print( k,  k<=numOnes,numOnes+numZeros)
        if k>=0 and k<=numOnes:
            return k
        elif k>= numOnes and k<=numOnes+numZeros:
            return numOnes
        else:
            return numOnes-(k-(numOnes+numZeros))
    print(kItemsWithMaximumSum( numOnes = 6, numZeros = 6, numNegOnes = 6, k = 13))
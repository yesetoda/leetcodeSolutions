def is_prime(n):
    if n<2:
        return False
    elif n<3 :
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i== 0:
            return False
    return True
class Solution:
    def countPrimeSetBits(left: int, right: int) -> int:
        primes = 0
        for i in range(left,right+1):
            if is_prime(bin(i)[2:].count("1")):
                primes+=1
                print(i,bin(i)[2:],bin(i)[2:].count("1"),is_prime(bin(i)[2:].count("1")))
        return primes
    print(countPrimeSetBits(left = 980, right = 1000))
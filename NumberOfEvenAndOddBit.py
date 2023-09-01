class Solution:
    def evenOddBit(n: int) -> list[int]:
        binar = bin(n)[2:][::-1]
        odds = 0
        evens = 0
        for ind,val in enumerate(binar):
            if val=="1":
                if ind%2==0:
                    evens+=1
                else:
                    odds+=1
        return [evens,odds]
    print(evenOddBit(17))

        
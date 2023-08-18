# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
        #  1 if num is lower than the picked number
        #  otherwise return 0
def guess(n,pick):
    return -1 if n>pick else 1 if n<pick else 0


class Solution:
    def guessNumber( n: int,pick) -> int:
        
        if guess(n,pick)==0:
            return n
        start = 1
        end =n
        mid  = (start+end)//2
        while True:
            # print(mid,(mid,pick))
            if guess(mid,pick) ==1:
                start = mid
                mid = (start+end)//2
            elif guess(mid,pick) ==-1:
                end = mid
                mid  = (start+end)//2
            elif guess(mid,pick) ==0:
                return mid


    print(guessNumber(2 ,2))
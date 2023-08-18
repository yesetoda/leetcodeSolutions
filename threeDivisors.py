class Solution:
    def isThree( n: int) -> bool:
        if n==4:
            return True
        if n%2==0:
            return False
        count = 0
        for i in range (5,n, 2):
            if n%i==0:
                count+=1
            if count>3:
                break
        return True if count==3 else False
    print(isThree(10346233))
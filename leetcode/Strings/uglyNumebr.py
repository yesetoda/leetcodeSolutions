class Solution:
    def isUgly(n: int) -> bool:
        while(True):
            if n==1 :
                return True
            if n==0:
                return False
            if n%2 ==0:
                n/=2
            elif n%3 ==0:
                n/=3
            elif n%5 ==0:
                n/=5
            else:return False      
        
    print(isUgly(0))
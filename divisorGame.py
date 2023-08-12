class Solution:
    def divisorGame(n: int) -> bool:
        x = 1
        count = 1
        while n>0 and x>0 and x<n :
            
            # print("!^^",x,n,count)
            if  n%x==0:
                n = n-x
                count+=1
            # else:
            #     x+=1
            print("^^",x,n,count)
        if count%2 == 0:
            return True
        else:return False
    print(divisorGame(4))
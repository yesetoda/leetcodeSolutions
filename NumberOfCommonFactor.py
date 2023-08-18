class Solution:
    def commonFactors( a: int, b: int) -> int:
        count = 0
        # for i in range(1,min(a,b)+1):
        #     if a%i ==0 and b%i==0:
        #         count+=1
        # return count
        ind = 1
        while ind<=min(a,b)+1:
            
            if a%ind ==0 and b%ind==0:
                count+=1
            if a%2==1 or b%2==1:
                ind+=2
            else:
                ind+=1 
        return count
    print(commonFactors(30,30))
    1,2,3,5,6,10,15,30
class Solution:
    def numberOfSteps( num: int) -> int:
        count = 0
        while(num!=0):
            if num%2 == 0:
                num/=2
                count+=1
            else:
                num-=1
                count+=1
        return count
        #     if int(num) &1 == 0:
        #         num/=2
        #         count+=1
        #     else:
        #             num-=1
        #             count+=1
        # return count
    
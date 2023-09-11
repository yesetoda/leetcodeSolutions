class Solution:
    def fillCups( amount: list[int]) -> int:
        
        count = 0
        while True:
            amount = sorted(amount,reverse = True)
            if amount[0]>0 and amount[1]>0:
                amount[0]-=1
                amount[1]-=1
                count+=1
                print("cond1",count,amount)
            elif amount[0]>0 and amount[2]>0:
                amount[0]-=1
                amount[2]-=1
                count+=1
                print("cond3",count,amount)
            elif amount[1]>0 and amount[2]>0:
                amount[1]-=1
                amount[2]-=1
                count+=1
                print("cond3",count,amount)
            else:
                break
            print("count",count)
        return count+sum(amount)
    print(fillCups(amount = [5,4,4]))

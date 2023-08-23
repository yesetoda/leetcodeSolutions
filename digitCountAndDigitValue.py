class Solution:
    def digitCount(num: str) -> bool:
        num = [i for i in num]
        for i in range(len(num)):
            # print(i,int(num[i]),num.count(str(i)),int(num[i]) != num.count(i))
            if int(num[i]) != num.count(str(i)):
                return False
            
        return True
    print(digitCount("030"))
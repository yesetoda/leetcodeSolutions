class Solution:
    def isAdditiveNumber( num: str) -> bool:
        for i in range(2,len(num)):
            if num[i] != str(eval(f"{num[i-1]}+{num[i-2]}")):
                return False
        return True
    print(isAdditiveNumber("199100199"))
class Solution:
    def sumOfNumberAndReverse(num: int) -> bool:
        # for i in range(num+1):
        #     if eval(f"{str(i)}+{int(str(i)[::-1])}") == num:
        #         return True
        # return False
        if num==0:
            return True
        for i in range(1, num + 1):
            reverse_i = int(str(i)[::-1])
            if i + reverse_i == num:
                return True
        return False
    print(sumOfNumberAndReverse(2))
from typing import Optional


class Solution:
    def addTwoNumbers(l1, l2):
        num1 = 0
        for i in range(len(l1)):
            num1+=l1[i]*10**(len(l1)-(i+1))
            print(l1[i],num1)
        num2 = 0
        for i in range(len(l2)):
            num2+=l2[i]*10**(len(l2)-(i+1))
            print(l2[i],num2)
        sumNum = num1+num2
        out = []
        for i in str(sumNum):
            out.append(int(i))
        return out
    print(addTwoNumbers( l1 = [0], l2 = [0]))

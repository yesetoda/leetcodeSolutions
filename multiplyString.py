class Solution:
    def multiply( num1: str, num2: str) -> str:
        return str(eval(num1+"*"+num2))
    num1 = "123"
    num2 = "456"
    print(multiply(num1,num2))
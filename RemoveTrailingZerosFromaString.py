class Solution:
    def removeTrailingZeros( num: str) -> str:
        return num.strip("0")
    print(removeTrailingZeros(  num = "123"  ))

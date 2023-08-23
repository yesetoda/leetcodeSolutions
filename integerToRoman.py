class Solution:
    def intToRoman( num: int) -> str:
        roman = {1000: 'M',900: 'CM',500: 'D',400: 'CD',100: 'C',90: 'XC',50: 'L',40: 'XL',10: 'X',9: 'IX',5: 'V',4: 'IV',1: 'I'}
        out = ""
        for value, symbol in roman.items():
            while num >= value:
                out += symbol
                num -= value
        return out

    print(intToRoman( 1994))
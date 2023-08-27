class Solution:
    def myAtoi(s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        elif s[0] in "+-":
            nums = s[0]
            s = s[1:]
        else:
            nums = "+"
        for i in s:
            if not i.isdecimal():
                break
            elif i.isdecimal():
                nums+=i
        n = int(nums) if len(nums)>1 else 0
        if n >=-2**31 and n<= (2**31) - 1:
            return n 
        elif  n <-2**31:
            return  -2**31
        elif  n >(2**31)-1:
            return  2**31-1
        
    print(myAtoi(s = "-12.4 with words"))
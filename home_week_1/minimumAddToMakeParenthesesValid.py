from random import choice
from time import perf_counter
class Solution:
    def minAddToMakeValid( s: str) -> int:
        if len(s)==0:
            return 0
        stack = [s[0]]
        for i in s[1:]:
            if stack and stack[-1]=="(" and i ==")":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
    s = ""
    for i in range(10000):
        s+=choice(["(",")"]) 
    a= perf_counter()
    print(minAddToMakeValid(s))
    b= perf_counter()
    print(b-a)

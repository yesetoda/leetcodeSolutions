# class Solution:
#     def backspaceCompare(s: str, t: str) -> bool:
#         sind = -1
#         tind = -1
#         while sind>=-len(s) and tind>=-len(t):
#             print(sind,tind,s[sind],t[tind])
#             if s[sind]=="#":
#                 sind-=1
#             if t[tind]=="#":
#                 tind-=1
#             if s[sind] == t[tind]:
#                 return False
#         return True
#     print(backspaceCompare( s = "a#c", t = "b" ))
class Solution:
    def backspaceCompare( s: str, t: str) -> bool:
        s_pointer = len(s) - 1
        t_pointer = len(t) - 1

        def find_next_valid_char(string: str, pointer: int) -> int:
            backspace_count = 0
            while pointer >= 0:
                if string[pointer] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    return pointer
                pointer -= 1
            return pointer

        while s_pointer >= 0 or t_pointer >= 0:
            s_pointer = find_next_valid_char(s, s_pointer)
            t_pointer = find_next_valid_char(t, t_pointer)

            if s_pointer < 0 and t_pointer < 0:
                return True
            if s_pointer < 0 or t_pointer < 0 or s[s_pointer] != t[t_pointer]:
                return False

            s_pointer -= 1
            t_pointer -= 1

        return True

    print(backspaceCompare(s = "ab#c", t = "ad#c"))
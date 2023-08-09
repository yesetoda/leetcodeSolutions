# # class Solution:
# #     def longestNiceSubstring(s: str) -> str:
# #         leng = len(set(s))
# #         if leng<2:
# #             return 0
        
# #         start = 0
# #         end = 0
# #         longest = 0
# #         char_count = 0
# #         char_found = {}
        
# #         for i in range(len(s)):
# #             if s[i] not in char_found:
# #                 char_found[s[i]] = s[i]
# #                 char_count+=1
        
# #     print(longestNiceSubstring( s = "YazaAay"))


# class Solution:
#     def longestNiceSubstring(s: str) -> str:
#         leng = len(set(s))
#         if leng<2:
#             return 0
        
#         start = 0
#         end = 1
#         longest = 0
#         char_count = 0
#         char_found = ""
        
#         for _ in range(20):
#             print(start,end,set(s[start:end].lower()),len(set(s[start:end])))
#             if len(set(s[start:end].lower())) <=2:
#                 end+=1
#             vset = set(s[start:end].lower())
#             if vset[0].upper() in set(s[start:end]) and vset[0].lower() in set(s[start:end]) and vset[1].upper() in set(s[start:end]) and vset[1].lower() in set(s[start:end]):
#                 if longest<len(s[start:end]):
#                     char_found = s[start:end]
#                     longest = len(char_found)
#                     print(char_found)
                
#             elif end==leng-1 and start==leng-1:
#                 break
            
#             else:
#                 start+=1
        
#     print(longestNiceSubstring( s = "YazaAay"))

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(substring):
            char_set = set(substring)
            for char in substring:
                if char.swapcase() not in char_set:
                    return False
            return True

        n = len(s)
        longest = ""

        for i in range(n):
            for j in range(i + len(longest), n):
                substring = s[i:j+1]
                if is_nice(substring) and len(substring) > len(longest):
                    longest = substring

        return longest


# Example usage and additional test cases

solution = Solution()

# Example 1
output = solution.longestNiceSubstring(s="YazaAay")
print(output)  # Output: "aAa"

# Example 2
output = solution.longestNiceSubstring(s="Bb")
print(output)  # Output: "Bb"

# Example 3
output = solution.longestNiceSubstring(s="c")
print(output)  # Output: ""

# Additional test cases

# Empty string
output = solution.longestNiceSubstring(s="")
print(output)  # Output: ""

# String with only one character
output = solution.longestNiceSubstring(s="a")
print(output)  # Output: ""

output = solution.longestNiceSubstring(s="A")
print(output)  # Output: ""

# String with all characters being the same (nice substring doesn't exist)
output = solution.longestNiceSubstring(s="bbbbbbb")
print(output)  # Output: ""

output = solution.longestNiceSubstring(s="AAAAA")
print(output)  # Output: ""

# String with all characters being nice
output = solution.longestNiceSubstring(s="AbBaAbB")
print(output)  # Output: "AbBaAbB"

output = solution.longestNiceSubstring(s="XYZxyzXYZ")
print(output)  # Output: "XYZxyzXYZ"

# String with multiple nice substrings
output = solution.longestNiceSubstring(s="abAB")
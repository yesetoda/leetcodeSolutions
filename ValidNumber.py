import re
class Solution:
    def isNumber( s: str) -> bool:
        # pat = r'^([-+]?)(\d+)[eE]?([.]?)(\d*)([eE]?\d+)?$'
        # return re.match(pat, s) is not None
        pat = r'^\s*[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?\s*$'
        return re.match(pat, s) is not None
    print(isNumber(s = "d234"))
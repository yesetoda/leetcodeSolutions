class Solution:
    def divisorSubstrings(num: int, k: int) -> int:
        out = 0
        numstr = str(num)
        for i in range(len(numstr)-(k-1)):
            if int(numstr[i:i+k])==0:
                pass
            elif num%(int(str(num)[i:i+k])) ==0:
                print(int(str(num)[i:i+k]),num%(int(str(num)[i:i+k])))
                out+=1
        return out
    print(divisorSubstrings(num = 2464, k = 4))
    
# numstr = "430043"
# k = 2
# out = 0
# for i in range(len(numstr)-(k-1)):
#     if int(numstr[i:i+k])==0:
#         pass
#     elif int(numstr)%(int(numstr[i:i+k])) ==0:
#         out+=1
# return out
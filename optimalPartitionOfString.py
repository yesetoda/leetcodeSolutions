from collections import Counter


class Solution:
    def partitionString( s: str) -> int:
        vis = set()
        count = 0
        for i in s:
            if i in vis:
                count+=1
                print(i,vis)
                vis = set(i)
                print(vis)
            else:
                vis.add(i)
            

        return max(count+1,Counter(s).most_common()[0][1])
    print(partitionString("hdklqkcssgxlvehv"))
class Solution:
    def minBitFlips( start: int, goal: int) -> int:
        start = bin(start)[2:][::-1]
        goal = bin(goal)[2:][::-1]
        maxi = max(len(goal),len(start))
        
        # print(start,goal)
        if len(start) == maxi:
            goal+="0"*(maxi-len(goal))
        else:
            start+="0"*(maxi-len(start))
        # print(start,goal)
        count = 0
        for i in range(maxi):
            if goal[i] != start[i]:
                count+=1
        return count
    print(minBitFlips(3,4))
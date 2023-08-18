class Solution:
    def findRelativeRanks(score: list[int]) -> list[str]:
        for ind,scr in enumerate(sorted(score[:],reverse = True)):
            if ind == 0:
                score[score.index(scr)] = "Gold Medal"
            elif ind ==1:
                score[score.index(scr)] = "Silver Medal"
            elif ind ==2:
                score[score.index(scr)] = "Bronze Medal"
            else:
                score[score.index(scr)] = str(ind+1)
        return score
    print(findRelativeRanks( score = [10,3,8,9,4]))
            
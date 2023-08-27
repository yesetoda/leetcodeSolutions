class Solution:
    def bestHand( ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) ==1:
            return "Flush"
        rank_set = set(ranks)
        maxSameRank= 0
        for i in rank_set:
            if ranks.count(i)>maxSameRank:
                maxSameRank = ranks.count(i)
        if maxSameRank>=3:
            return "Three of a Kind"
        elif maxSameRank==2:
            return "Pair"
        elif maxSameRank ==1:
            return "High Card"
    print(bestHand(ranks = [1,1,1,1,1], suits = ["b","a","a","a","a"]))
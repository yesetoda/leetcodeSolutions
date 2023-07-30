class Solution:
    def maximumWealth( accounts: list[list[int]]) -> int:
        return max([sum(i) for i in accounts])
    print(maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]]))
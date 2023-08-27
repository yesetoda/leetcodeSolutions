class Solution:
    def removeStones(stones: list[list[int]]) -> int:
        rows = {}
        cols = {}
        count = 0
        for stone in stones:
            row, col = stone[0], stone[1]
            if row not in rows and col not in cols:
                # count += 1
                pass
            elif row in rows:
                count += 1
            elif  col in cols:
                count+=1
            rows[row] = 1
            cols[col] = 1
        return count
    print(removeStones(stones = [[0,1],[1,0],[1,1]]))
class Solution:
    def numRookCaptures( board: list[list[str]]) -> int:
        rook_pos = [-1,-1]
        for i in range(len(board)):
            if "R" in board[i]:
                rook_pos = [i,board[i].index("R")]
                break
        count = 0
        #up
        up = rook_pos[:]
        while up[0]>=1:
            up = [up[0]-1,up[1]]
            if board[up[0]][up[1]] == "B":
                break
            elif board[up[0]][up[1]] == "p":
                count+=1
                break
        #down
        down = rook_pos[:]
        while down[0]<=6:
            down = [down[0]+1,down[1]]
            if board[down[0]][down[1]] == "B":
                break
            elif board[down[0]][down[1]] == "p":
                count+=1
                break
        #left
        left = rook_pos[:]
        while left[1]>=1:
            left = [left[0],left[1]-1]
            if board[left[0]][left[1]] == "B":
                break
            elif board[left[0]][left[1]] == "p":
                count+=1
                break
        #right
        right = rook_pos[:]
        while right[1]<=6:
            right = [right[0],right[1]+1]
            if board[right[0]][right[1]] == "B":
                break
            elif board[right[0]][right[1]] == "p":
                count+=1
                break
        return count
    print(numRookCaptures(board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
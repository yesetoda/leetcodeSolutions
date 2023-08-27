class Solution:
    def tictactoe( moves: list[list[int]]) -> str:
        grid =   [[" "," "," "],[" "," "," "],[" "," "," "]]
        for ind,pos in enumerate(moves):
            if ind%2==0:
                grid[pos[0]][pos[1]]="X"
            else:
                grid[pos[0]][pos[1]]="O"
        #row winner
        for i in grid:
            if i.count("X")==3:
                return "A"
            elif i.count("O")==3:
                return "B"
        #column winner
        for cl in range(len(grid)):
            if [grid[0][cl],grid[1][cl],grid[2][cl]].count("X") == 3:
                return "A"
            elif  [grid[0][cl],grid[1][cl],grid[2][cl]].count("O") == 3:
                return "B"
        #positive diagonal winner
        if [grid[0][0],grid[1][1],grid[2][2]].count("X")==3:
            return "A"
        if [grid[0][0],grid[1][1],grid[2][2]].count("O")==3:
            return "B"
        #negative diagonal winner
        if [grid[0][2],grid[1][1],grid[2][0]].count("X")==3:
            return "A"
        if [grid[0][2],grid[1][1],grid[2][0]].count("O")==3:
            return "B"
        for i in grid:
            if i.count(" ")>0:
                return "Pending"
        return "Draw"
    print(tictactoe(moves = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,1],[2,0]]))
            

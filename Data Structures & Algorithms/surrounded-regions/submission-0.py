class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r,c):
            if r not in range(1,ROWS-1) or c not in range(1,COLS-1) or board[r][c] !="O":
                return
            
            board[r][c] = "X"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(1,ROWS-1):
            for c in range(1,COLS-1):
                if board[r][c] == "O":
                    dfs(r,c)
        

        
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        numIslands = 0

        def dfs(row, col):
            if row not in range(rows) or col not in range(cols) or grid[row][col] == '0':
                return

            grid[row][col] = '0'

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    numIslands += 1
                    dfs(r, c)
                    
        
        return numIslands
        
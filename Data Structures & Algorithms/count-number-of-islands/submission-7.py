class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        num_islands = 0

        def dfs(x, y):
            if not x in range(ROWS) or not y in range(COLS) or grid[x][y] != '1':
                return None
            
            grid[x][y] = '0'

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

            return


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands
        
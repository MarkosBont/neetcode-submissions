class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0


        def dfs(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == "0":
                return 

            grid[x][y] = "0"

            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)

            return


        for row in range(ROWS):
            for col in range (COLS):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count


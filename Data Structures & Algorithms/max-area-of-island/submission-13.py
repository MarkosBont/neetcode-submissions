class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        maxArea = 0

        def dfs(x, y):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0:
                return 0 

            grid[x][y] = 0

            return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)

        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    maxArea = max(maxArea, area)
        
        return maxArea

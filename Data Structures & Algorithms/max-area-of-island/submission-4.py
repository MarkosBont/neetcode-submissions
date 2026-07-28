class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        n_rows = len(grid)
        n_cols = len(grid[0])

        def dfs(row, col):
            if row not in range(n_rows) or col not in range(n_cols) or grid[row][col] == 0:
                return 0 
            
            grid[row][col] = 0

            return 1 + dfs(row, col-1)+ dfs(row, col+1)+ dfs(row-1, col)+ dfs(row+1, col)


        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1:
                    area = dfs(row,col)
                    maxArea = max(maxArea, area)
        
        return maxArea
        
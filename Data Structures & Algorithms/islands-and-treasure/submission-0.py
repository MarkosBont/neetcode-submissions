class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n_rows = len(grid)
        n_cols = len(grid[0])

        visited = set()

        q = deque()

        def addCell(r, c):
            if r not in range(n_rows) or c not in range(n_cols) or (r,c) in visited or grid[r][c] == -1:
                return
            
            q.append((r,c))
            visited.add((r,c))

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = distance

                addCell(r-1, c)
                addCell(r+1, c)
                addCell(r, c-1)
                addCell(r, c+1)
            
            distance += 1
                
        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        minutes = 0
        freshOranges = 0
        q = deque()
        visited = set()

        def addCell(r,c):
            if r not in range(n_rows) or c not in range(n_cols) or grid[r][c] != 1 or (r,c) in visited:
                return
            
            q.append((r,c))
            visited.add((r,c))

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    freshOranges += 1
        
        if freshOranges == 0:
            return 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    freshOranges -= 1

                grid[r][c] = 2

                addCell(r-1,c)
                addCell(r+1,c)
                addCell(r,c-1)
                addCell(r,c+1)
            
            if freshOranges == 0:
                return minutes
            minutes += 1
        
        return -1



        
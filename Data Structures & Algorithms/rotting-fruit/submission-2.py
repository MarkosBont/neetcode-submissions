class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        minutes = 0
        q = deque()
        visited = set()

        def freshFruits():
            for r in range(n_rows):
                for c in range(n_cols):
                    if grid[r][c] == 1:
                        return True
            
            return False

        if not freshFruits():
            return minutes

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

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                addCell(r-1,c)
                addCell(r+1,c)
                addCell(r,c-1)
                addCell(r,c+1)
            
            if not freshFruits():
                return minutes
            minutes += 1
        
        return -1



        
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))

        def addToQ(i,j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0 or (i,j) in visited:
                return None
            
            grid[i][j] = 2
            q.append((i,j))
            visited.add((i,j))
        
        def checkComplete(grid):
            ROWS = len(grid)
            COLS = len(grid[0])

            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1:
                        return False
            
            return True

        
        minutes = -1
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()

                addToQ(i-1, j)
                addToQ(i+1, j)
                addToQ(i, j-1)
                addToQ(i, j+1)
            
            minutes += 1
        
        if checkComplete(grid):
            return minutes

        return -1

        
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        minutes = 0
        numFresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    numFresh += 1
        
        if numFresh == 0:
            return 0

        def addToQ(i,j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] != 1:
                return None
            
            q.append((i,j))
        
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                if grid[i][j] == 1:
                    numFresh -= 1
                    if numFresh == 0:
                        return minutes
                        
                grid[i][j] = 2

                addToQ(i-1, j)
                addToQ(i+1, j)
                addToQ(i, j-1)
                addToQ(i, j+1)
            
            minutes += 1

        return -1

        
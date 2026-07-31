import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        minutes = 0
        numFresh = 0

        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numFresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        if numFresh == 0:
            return 0
        
        def addToQueue(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            
            q.append((r,c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    numFresh -= 1
                    if numFresh == 0:
                        return minutes

                grid[r][c] = 2

                addToQueue(r-1,c)
                addToQueue(r+1,c)
                addToQueue(r,c-1)
                addToQueue(r,c+1)

            minutes += 1
                
        return -1
        
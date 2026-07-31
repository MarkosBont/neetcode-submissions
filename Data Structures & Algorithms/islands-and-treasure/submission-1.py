from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))
        
        def addToQueue(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 2147483647 or (r,c) in visited:
                return
            
            visited.add((r,c))
            q.append((r,c))


        distance = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance

                addToQueue(r+1, c)
                addToQueue(r-1, c)
                addToQueue(r, c-1)
                addToQueue(r, c+1)
            
            distance += 1
        
        
        
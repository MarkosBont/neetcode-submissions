class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))

        def addToQ(i,j):
            if i < 0 or i >= ROWS or j < 0 or j>= COLS or grid[i][j] != 2147483647 or (i,j) in visited:
                return

            visited.add((i,j))
            q.append((i,j))
        
        distance = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance

                addToQ(r-1,c)
                addToQ(r+1,c)
                addToQ(r,c-1)
                addToQ(r,c+1)
            
            distance += 1
    
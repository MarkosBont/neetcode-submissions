from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        q = deque()
        minutes = 0
        self.num_fresh = 0

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] == 2:
                    q.append((row, col))

                elif grid[row][col] == 1:
                    self.num_fresh += 1
        
        def check_and_append(x,y):
            if x < 0 or x >= self.ROWS or y <0 or y >= self.COLS or grid[x][y] == 0 or grid[x][y] == 2:
                return
            
            grid[x][y] = 2
            self.num_fresh -= 1
            q.append((x, y))


        if self.num_fresh == 0:
            return 0

        while q and self.num_fresh > 0:
            for _ in range(len(q)):
                x, y = q.popleft()

                check_and_append(x-1,y)
                check_and_append(x+1,y)
                check_and_append(x,y-1)
                check_and_append(x,y+1)
            
            minutes += 1
        

        if self.num_fresh == 0:
            return minutes
        
        return -1
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        seen = set()

        distance_from_treasure = 0

        for row in range(ROWS):
            for col in range(COLS):
                value = grid[row][col]
                if value == 0:
                    q.append((row, col))
        
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == -1 or (x,y) in seen:
                    continue

                grid[x][y] = distance_from_treasure
                seen.add((x,y))

                q.append((x-1, y))
                q.append((x+1, y))
                q.append((x,y-1))
                q.append((x,y+1))
            
            distance_from_treasure += 1

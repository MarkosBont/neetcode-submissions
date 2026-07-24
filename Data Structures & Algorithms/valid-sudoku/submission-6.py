def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen and num != '.':
            return True
        
        seen.add(num)
    
    return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if contains_duplicate(row):
                return False
        
        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if contains_duplicate(col):
                return False
        
        for row_grid in range(0,9,3):
            for col_grid in range(0,9,3):
                grid = []
                for i in range(row_grid, row_grid+3):
                    for j in range(col_grid, col_grid+3):
                        grid.append(board[i][j])
                
                if contains_duplicate(grid):
                    return False
        
        return True


        
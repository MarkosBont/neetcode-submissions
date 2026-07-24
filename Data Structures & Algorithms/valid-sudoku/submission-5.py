def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num == '.':
            continue

        if num in seen:
            return True
        
        seen.add(num)
    
    return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row checking
        for i in range(9):
            if contains_duplicate(board[i]):
                return False

        # Column checking
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if contains_duplicate(column):
                return False

        # Grid checking
        for row_block in range(0,9,3):
            for col_block in range(0,9,3):
                grid = []
                for i in range(3):
                    for j in range(3):
                        grid.append(board[row_block+i][col_block + j])
                
                if contains_duplicate(grid):
                    return False

        return True



        



        
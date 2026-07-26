class Solution:
    def hasDuplicate(self, elements):
        seen = set()
        for num in elements:
            if num == '.':
                continue
            
            if num in seen:
                return True
            
            seen.add(num)

        return False


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row checking
        for row in board:
            if self.hasDuplicate(row):
                return False

        # Column Checking
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if self.hasDuplicate(column):
                return False
        
        # Grid checking
        for row_block in range(0,9,3):
            for col_block in range(0,9,3):
                grid = []
                for i in range(row_block, row_block+3):
                    for j in range(col_block, col_block+3):
                        grid.append(board[i][j])

                if self.hasDuplicate(grid):
                    return False
        
        return True



        


        
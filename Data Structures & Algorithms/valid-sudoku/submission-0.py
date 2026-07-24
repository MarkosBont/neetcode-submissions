def contains_duplicates(nums):
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
        # Row by row checking
        for i in range(9):
            row = board[i]
            if contains_duplicates(row):
                return False
        
        # Column by columm checking
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if contains_duplicates(column):
                return False
        
        #3x3 checking
        for row_start in range(0,9,3):
            for column_start in range(0,9,3):
                grid = []
                for i in range(row_start, row_start+3):
                    for j in range(column_start, column_start+3):
                        grid.append(board[i][j])
                
                if contains_duplicates(grid):
                    return False
        
        return True



                


        
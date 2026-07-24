def contains_duplicate(nums:List[int]):
    num_set = set()
    for num in nums:
        if num == '.':
            continue

        if num in num_set:
            return True
        
        num_set.add(num)
    
    return False


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row Checking
        for i in range(9):
            row = board[i]
            if contains_duplicate(row):
                return False

        # Column checking
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if contains_duplicate(column):
                return False
        
        # Grid Checking
        for row_block in range(0, 9, 3):
            for column_block in range(0, 9, 3):
                grid = []
                for i in range(3):
                    for j in range(3):
                        grid.append(board[row_block + i][column_block + j])
                
                if contains_duplicate(grid):
                    return False
        
        return True


            


        
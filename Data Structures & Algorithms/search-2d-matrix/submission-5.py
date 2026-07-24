class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            
            elif target < matrix[row][0]:
                bot = row - 1
            
            else:
                break
        
        if not (top <= bot):
            return False
        
        l = 0
        r = cols

        while l <= r:
            middle = (l + r) // 2

            if matrix[row][middle] == target:
                return True
            
            elif matrix[row][middle] < target:
                l = middle + 1
            
            else:
                r = middle - 1
        
        return False
        
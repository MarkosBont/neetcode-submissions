class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1
        row = None

        while up <= down:
            middle = (up + down) // 2
            if target <= matrix[middle][-1] and target >= matrix[middle][0]:
                row = matrix[middle]
                break
            
            elif target < matrix[middle][0]:
                down = middle - 1
            
            else:
                up = middle + 1
        
        if not row:
            return False
        
        l = 0
        r = len(row) - 1

        while l <= r:
            middle = (l+r) // 2
            if target == row[middle]:
                return True
            
            elif target < row[middle]:
                r = middle - 1
            
            else:
                l = middle + 1
        
        return False


        
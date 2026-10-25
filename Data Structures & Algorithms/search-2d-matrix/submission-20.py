class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        row = None
        
        while left <= right:
            midpoint = (left+right) // 2
            candidate_row = matrix[midpoint]
            if target < candidate_row[0]:
                right = midpoint - 1
            elif target > candidate_row[-1]:
                left = midpoint + 1
            else:
                row = candidate_row
                break
        
        if row is None:
            return False
        
        left = 0
        right = len(row) - 1
        
        while left <= right:
            midpoint = (left + right ) // 2
            element = row[midpoint]
            
            if target > element:
                left = midpoint + 1
            elif target < element:
                right = midpoint - 1
            else:
                return True

        return False

            
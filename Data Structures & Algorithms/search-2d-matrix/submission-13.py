class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)
        row = None
        

        while left <= right:
            middle = (left + right) // 2
            mid_row = matrix[middle]

            if target < mid_row[0]:
                right = middle - 1
            
            elif target > mid_row[-1]:
                left = middle + 1
            
            else:
                row = mid_row
                break

        
        left = 0
        right = len(row)
        if not row:
            return False

        while left <= right:
            middle = (left + right) // 2
            mid_elem = row[middle]

            if target == mid_elem:
                return True
            
            elif target < mid_elem:
                right = middle - 1
            
            else:
                left = middle + 1
        
        return False
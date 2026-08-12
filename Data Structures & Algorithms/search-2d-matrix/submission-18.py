class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)-1
        final_row = None

        while top <= bot:
            mid = (top + bot) // 2
            row = matrix[mid]

            if target < row[0]:
                bot = mid - 1
            
            elif target > row[-1]:
                top = mid + 1
            
            else:
                final_row = row
                break
        

        if not final_row:
            return False
        
        l = 0
        r = len(final_row) - 1

        while l <= r:
            mid = (l + r) // 2
            result = final_row[mid]
            if result == target:
                return True
            
            elif result < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False

        
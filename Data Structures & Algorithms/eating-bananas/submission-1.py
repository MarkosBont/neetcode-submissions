class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        lowest_k = max(piles)
        minimum_hours = float('inf')

        while low <= high:
            piles_copy = piles.copy()
            middle = (high + low) // 2

            hours_taken = 0
            for pile in piles_copy:
                while pile > 0:
                    hours_taken += 1
                    pile -= middle
            
            if hours_taken < minimum_hours:
                minimum_hours = hours_taken
                lowest_k = middle
            
            if hours_taken <= h:
                high = middle - 1
            
            else:
                low = middle + 1
        
        return lowest_k



        
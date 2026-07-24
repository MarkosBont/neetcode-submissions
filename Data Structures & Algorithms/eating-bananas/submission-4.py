class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        lowest_k = max(piles)
        minimum_hours = float('inf')

        while low <= high:
            middle = (high + low) // 2
            hours_taken = 0

            for pile in piles:
                hours_taken += math.ceil(pile/middle)

            
            if hours_taken <= h:
                lowest_k = middle
                high = middle - 1
            
            else:
                low = middle + 1
        
        return lowest_k



        
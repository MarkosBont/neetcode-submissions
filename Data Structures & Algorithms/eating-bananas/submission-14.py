class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1

        current_min = max_k

        while min_k <= max_k:
            mid = (min_k + max_k) // 2

            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile/mid)
            
            if hours_taken > h:
                min_k = mid + 1

            elif hours_taken <= h:
                current_min = mid
                max_k = mid - 1

        
        return current_min
                

        
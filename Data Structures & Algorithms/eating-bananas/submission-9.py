class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_k = max(piles)
        lower_k = 1
        k = float('inf')

        while lower_k <= upper_k:
            mid = (lower_k + upper_k) // 2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/mid)

            if time_taken > h:
                lower_k = mid + 1

            if time_taken <= h and mid < k:
                k = mid
                upper_k = mid - 1

        
        return k

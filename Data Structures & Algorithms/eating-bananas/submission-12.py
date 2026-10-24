class Solution:
    def test_k(self, k, piles, h ):
        time_taken = 0
        for pile in piles:
            time_taken += math.ceil(pile/k)
        
        return time_taken <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        possible_k = []
        max_k = max(piles)
        curr_min = max_k

        for i in range(1, max_k+1):
            possible_k.append(i)
        
        l = 1
        r = max_k
        while l <= r:
            k = (l+r) // 2
            if self.test_k(k, piles, h) and k < curr_min:
                curr_min = k
                r = k - 1
            
            elif not self.test_k(k, piles, h):
                l = k + 1
            
            else:
                r = k - 1

        
        return curr_min
            




        
        
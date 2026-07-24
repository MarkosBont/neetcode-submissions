class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final_profit = 0
        lowest = float('inf')

        for price in prices:
            if price < lowest:
                lowest = price
                continue
            
            profit = price - lowest
            final_profit = max(final_profit, profit)
        
        return final_profit
        
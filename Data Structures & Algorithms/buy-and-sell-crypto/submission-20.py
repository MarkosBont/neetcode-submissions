class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy = 0
        sell = 0 
        
        for i, price in enumerate(prices):
            if price < prices[buy]:
                buy = i

            else:
                profit = price - prices[buy]
                maxProfit = max(maxProfit, profit)
        
        return maxProfit

        
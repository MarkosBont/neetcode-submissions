class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0

        maxProfit = 0

        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, profit)
            
            else:
                buy = sell

        return maxProfit
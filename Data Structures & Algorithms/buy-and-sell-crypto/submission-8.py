class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maxProf = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxProf = max(maxProf, profit)
            else:
                buy = sell
            sell += 1
        
        return maxProf



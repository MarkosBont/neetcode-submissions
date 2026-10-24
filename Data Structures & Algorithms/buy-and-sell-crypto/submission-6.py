class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = 1
        maxProf = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[buy] - prices[sell]
                maxProf = max(maxProf, profit)
            else:
                buy = sell
            sell += 1
        
        return maxProf



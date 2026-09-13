class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        curr_max = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            
            else:
                this_profit = prices[i] - buy
                curr_max = max(curr_max, this_profit)
        
        return curr_max

        
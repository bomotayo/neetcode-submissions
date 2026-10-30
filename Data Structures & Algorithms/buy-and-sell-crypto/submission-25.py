class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,profit,max_profit = 0,0,0

        for sell in range(len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit,max_profit)
        
        return max_profit
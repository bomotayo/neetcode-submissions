class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            diff = prices[sell] - prices[buy]
            profit = max(diff, profit)

        return profit


        
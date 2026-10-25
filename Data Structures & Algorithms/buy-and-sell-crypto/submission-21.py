class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0

        for sell in range(len(prices)):
            while prices[sell] < prices[buy]:
                buy += 1
            diff = prices[sell] - prices[buy]
            profit = max(diff, profit)

        return profit


        
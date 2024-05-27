# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def f(self, day, can_buy, transactions_left, total_days, prices, memo):
        if day == total_days or transactions_left == 0:
            return 0
        if memo[day][can_buy][transactions_left] != -1:
            return memo[day][can_buy][transactions_left]
        if can_buy:
            buy = -prices[day] + self.f(day + 1, 0, transactions_left, total_days, prices, memo)
            skip = self.f(day + 1, 1, transactions_left, total_days, prices, memo)
            profit = max(buy, skip)
        else:
            sell = prices[day] + self.f(day + 1, 1, transactions_left - 1, total_days, prices, memo)
            hold = self.f(day + 1, 0, transactions_left, total_days, prices, memo)
            profit = max(sell, hold)
        memo[day][can_buy][transactions_left] = profit
        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        total_days = len(prices)
        memo = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(total_days)]
        return self.f(0, 1, 2, total_days, prices, memo)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_prices:
                min_prices = price
            else:
                profit = price - min_prices
                if profit > max_profit:
                    max_profit = profit    
        return max_profit
        
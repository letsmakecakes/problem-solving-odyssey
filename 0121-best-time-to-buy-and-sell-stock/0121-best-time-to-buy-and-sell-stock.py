class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] # Directly initialize with the first price
        max_profit = 0

        for price in prices[1:]:    # Start from the second element
            if price < min_price:
                min_price = price   # Update min_price
            elif price - min_price > max_profit:
                max_profit = price - min_price # Update max_profit
        
        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate maximum profit from buying and selling stock once.

        Args:
            prices: List of stock prices where prices[i] is the price on day i

        Returns:
            Maximum profit achievable, or 0 if no profit possible
        """
        if len(prices) < 2:
            return 0
        
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
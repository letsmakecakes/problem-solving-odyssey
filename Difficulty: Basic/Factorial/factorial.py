class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        """
        Calculate factorial of n using recursion.
        
        Args:
            n: Non-negative integer
        
        Returns:
            Fatorial of n (n!)
        """
        if n <= 1:
            return 1
        
        return n * self.factorial(n - 1)
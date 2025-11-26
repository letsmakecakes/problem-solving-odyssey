class Solution:
    def findSum(self, n):
        """Calculate sum of numbers from 1 to n using recursion."""
        if n <= 0:
            return 0
        return n + self.findSum(n - 1)
        

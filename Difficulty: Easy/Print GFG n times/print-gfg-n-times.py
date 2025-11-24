#User function Template for python3

class Solution:
    def printGfg(self, n):
        """
        Print 'GFG' n times using recursion.
        
        Args:
            n: Number of times to print 'GFG'
        """
        if n <= 0:
            return
        
        print("GFG", end=" ")
        self.printGfg(n - 1)
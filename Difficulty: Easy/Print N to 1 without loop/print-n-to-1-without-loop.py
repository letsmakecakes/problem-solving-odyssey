#User function Template for python3

class Solution:
    def printNos(self, n):
        """Print numbers from n down to 1 in descending order."""
        if n > 0:
            print(n, end=" ")
            self.printNos(n - 1)
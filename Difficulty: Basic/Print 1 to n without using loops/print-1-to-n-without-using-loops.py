class Solution:
    def printTillN(self, N):
        """
        Print numbers from 1 to n using recursion.
        
        Args:
            N: The upper limit (inclsuive) of numbers to print
        """
    	if N <= 0:
    	    return
    	
    	self.printTillN(N - 1)
    	print(N, end=" ")
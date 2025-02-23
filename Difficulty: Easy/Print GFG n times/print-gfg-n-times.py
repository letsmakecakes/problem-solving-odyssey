#User function Template for python3

class Solution:
    def printGfg(self, n):
        """
        Recursively prints 'GFG' n times without using loops.
        
        Args:
            n (int): Number of times to print 'GFG'
        
        Returns:
            None: Prints output to standard output
        
        Raises:
            ValueError: If n is negative
            TypeError: If n is not an integer
        """
        # Input validation
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("input must be non-negative")
        
        # Base case
        if n == 0:
            return
        
        # Recursive case: print GFG n-1 times, then print once more
        self.printGfg(n - 1)
        print("GFG", end=' ')


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
        print("~")
# } Driver Code Ends
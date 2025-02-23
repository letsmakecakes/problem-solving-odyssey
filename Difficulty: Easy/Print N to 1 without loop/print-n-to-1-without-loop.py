#User function Template for python3

class Solution:
    def printNos(self, n):
        """
        Recursively prints numbers from n to 1 in decreasing order.
        
        Args:
            n (int): The starting number to print from
        
        Returns:
            None: Prints numbers to standard output
        
        Raises:
            ValueError: If n is negative
            TypeError: If n is not an integer
        """
        # Input validation
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Input must be non-negative")
        
        # Base case
        if n == 0:
            return
        
        # Print current number first (descending order)
        print(n, end=' ')
        
        # Then make recursive call
        self.printNos(n - 1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
        print("~")
# } Driver Code Ends
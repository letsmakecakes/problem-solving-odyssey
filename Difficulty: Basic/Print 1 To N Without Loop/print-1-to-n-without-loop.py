#User function Template for python3

class Solution:    
    def printNos(self,n):
        """
        Recursively prints numbers from 1 to n without using loops.
        
        Args:
            n (int): The upper limit of numbers to print
        
        Returns:
            None: Prints numbers to standard output
        
        Raises:
            ValueError: If n is negative
        """
        # Input validation
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0:
            raise ValueError("Input must be non-negative")
        
        # Base case
        if n == 0:
            return
        
        # Recursive case: print numbers 1 to n-1, then print n
        self.printNos(n - 1)
    
        print(n, end=' ')


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        ob = Solution()

        ob.printNos(N)
        print()
        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
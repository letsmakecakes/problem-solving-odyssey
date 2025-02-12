#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def countNodes(self, i):
        """
        Calculate the number of nodes at a given level in a perfect binary tree.
        
        Args:
            i (int): The level number (1-based indexing)
        
        Returns:
            ValueError: If level is less than 1
        """
        if i < 1:
            raise ValueError("Level must be a positive integer")
        
        # In a perfect binary tree, number of nodes at level i is 2^(i-1)
        return 2 ** (i - 1)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        i = int(input())
        ob = Solution()
        res = ob.countNodes(i)
        print(res)
        print("~")
# } Driver Code Ends
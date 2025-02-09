#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        """
        Calculate the minimum difference between maximum and minimum heights after modifying eacg height by +k or -k.
        
        Args:
            arr (List[int]): List of tower heights
            k (int): The value by which heights can be increased or decreased
        
        Returns:
            int: Minimum difference between maximum and minimum heights
        
        Raises:
            ValueError: If array is empty of k is negative
        """
        if not arr:
            raise ValueError("Array cannot be empty")
        if k < 0:
            raise ValueError("k must be non-negative")
        
        n = len(arr)
        if n == 1:
            return 0
        
        # Sort the array to handle heights systematically
        arr.sort()
        
        # Initialize result as difference between original max and min
        result = arr[n-1] - arr[0]
        
        for i in range(n-1):
            # Get maximum and minimum possible values for current index
            max_height = max(arr[n-1] - k, arr[i] + k)
            min_height = min(arr[0] + k, arr[i+1] - k)
            new_height = 0
            
            # If negative height would result, skip this iteration
            if min_height < 0:
                continue
            
            # Update result if new difference is smaller
            result = min(result, max_height - min_height)
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends
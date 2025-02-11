#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        """
        Sort the array using an optimized bubble sort algorithm.
        
        Args:
            arr: List[int] - The input array to be sorted
        
        Returns:
            List[int] - The sorted array
        
        """
        n = len(arr)
        if n <= 1:
            return arr
            
        for i in range(n - 1):
            # Flag to detect if any swapping occurred
            swapped = False
            
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # Compare adjacent elements
                if arr[j] > arr[j + 1]:
                    # Swap if they are in wrong order
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            # If no swapping occurred in this pass,
            # array is already sorted
            if not swapped:
                break
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
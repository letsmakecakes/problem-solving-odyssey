class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        """
        Counts frequency of elements from 1 to N in the array where N is array length.
        
        Args:
            arr (List[int]): Input array of integers
        
        Returns:
            List[int]: List containing frequencies of elements from 1 to N
        """
        n = len(arr)
        # Initialize result array with zeros
        frequencies = [0] * n
        
        # Count frequencies using array indexing
        for num in arr:
            if 1 <= num <= n: # Only count numbers in valid range
                frequencies[num - 1] += 1
        
        return frequencies



#{ 
 # Driver Code Starts
# Main code to read input and process each test case
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().frequencyCount(arr)  # find the frequencies

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print the result
    else:
        print("[]")  # Print empty list if no valid frequencies

# } Driver Code Ends
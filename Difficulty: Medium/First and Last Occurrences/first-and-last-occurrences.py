#User function Template for python3


class Solution:
    def find(self, arr, x):
        if not arr: # Handle empty array
            return [-1, -1]
            
        first, last = -1, -1
        
        #Single pass through the array
        for i, num in enumerate(arr):
            if num == x:
                if first == -1: # First occurrence
                    first = i
                last = i # Update the las occurrence
        
        return [first, last]

#{ 
 # Driver Code Starts
t = int(input())  # Number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array for each test case
    x = int(input())  # Element to search for
    ob = Solution()
    ans = ob.find(arr, x)  # Call the find function in the Solution class
    print(*ans)  # Print the result as space-separated values
    print("~")

# } Driver Code Ends
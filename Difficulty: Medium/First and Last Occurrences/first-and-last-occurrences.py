#User function Template for python3


class Solution:
    def find(self, arr, x):
        # Find the first and last occurences of x in arr
        occurences = [i for i, num in enumerate(arr) if num == x]
        
        # Return the first and last occurences
        if occurences:
            return [occurences[0], occurences[-1]]
        else:
            return [-1, -1]  # Return [-1, -1] if x is not found

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
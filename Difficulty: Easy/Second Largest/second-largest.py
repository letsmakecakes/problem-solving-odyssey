class Solution:
    def getSecondLargest(self, arr):
        first_max = -1
        second_max = -1
        
        for digit in arr:
            if digit > first_max:
                second_max = first_max
                first_max = digit
            elif digit != first_max and digit > second_max:
                second_max = digit
        
        return second_max

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends
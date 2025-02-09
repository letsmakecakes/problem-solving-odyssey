#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    """
	    Find minimum number of jumps needed to reach the end of array.
	    Each element represents the maximum number of steps that can be made forward from that element.
	    
	    Args:
	        arr (list): List of integers where arr[i] represents maximum jump length at position i
	   
	    Retuns:
	        int: Minimum number of jumps to reach end, -1 if not possible
	    """
	    if not arr or len(arr) <= 1:
	        return None
	    
	    if arr[0] == 0:
	        return -1
	    
	    n = len(arr)
	    max_reach = arr[0] # Maximum index we can reach from current position
	    steps_remaining = arr[0] # Steps we can still take in current jump
	    jumps = 1 # We already took first jump
	    
	    for i in range(1, n - 1): # We don't need to jump from last index
	        # Update max_reach for current_index
	        max_reach = max(max_reach, i + arr[i])
	        
	        # Used up a step to get to current index
	        steps_remaining -= 1
	        
	        # If we can't move forward
	        if steps_remaining == 0:
	            # Must take a jump if possible
	            jumps += 1
	            
	            # If we can't reach any further
	            if i >= max_reach:
	                return -1
	           
	            # Update steps we can take in new jump
	            steps_remaining = max_reach - i
	    
	    return jumps if max_reach >= n - 1 else -1
	        
	        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends
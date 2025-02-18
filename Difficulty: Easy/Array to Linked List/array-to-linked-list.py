#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        """
        Construct a linked list from an array of integers.
        
        Args:
            arr (list): List of integers to convert to linked list
        
        Returns:
            Node: Head of the constructed linked list
        """
        # Handle edge case of empty array
        if not arr:
            return None
        
        # Create the head node with the first element
        head = Node(arr[0])
        current = head
        
        # Iterate through remaining elements and add nodes
        for num in arr[1:]:
            current.next = Node(num)
            current = current.next
        
        return head
        
        return dummy_node.next

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        # n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
        print("~")
# } Driver Code Ends
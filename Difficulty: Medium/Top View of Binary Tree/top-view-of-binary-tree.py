#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        if not root:
            return []
        
        top_view_map = {} # Dictionary to store the top view nodes
        queue = [[root, 0]] # Queue for level order traversal, storing node and its horizontal distance
        while queue:
            current, hd = queue.pop(0)
            
            # If horizontal distance is seeing for the first time
            if hd not in top_view_map:
                top_view_map[hd] = current
            
            # Add left and right children to the queue
            if current.left:
                queue.append([current.left, hd - 1])
            
            if current.right:
                queue.append([current.right, hd + 1])
        
        # Extracting the top view nodes from the map
        min_hd = min(top_view_map.keys())
        max_hd = max(top_view_map.keys())
        
        top_view = [top_view_map[hd].data for hd in range(min_hd, max_hd + 1)]
        
        return top_view


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        ob = Solution()

        res = ob.topView(root)
        for i in res:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends
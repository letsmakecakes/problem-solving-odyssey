from collections import deque

''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

class Solution:
    def leftView(self, root):
        """
        Returns the left view of a binary tree using level-order traversal.
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            List of values representing the left view of the tree
        """
        # Handle edge case: empty tree
        if not root:
            return []
            
        queue = deque([root])
        left_view = []
        
        while queue:
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()
                
                # First node at each level is part of left view
                if i == 0:
                    left_view.append(node.data)
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        
        return left_view